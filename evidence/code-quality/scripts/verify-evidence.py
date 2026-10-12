#!/usr/bin/env python3
"""Verify original, unchanged Code Quality artifact provenance and final gate.

This is an offline evidence-integrity verifier, NOT a .NET or SonarQube run.
"""
import hashlib
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [('01-pre-coverage-baseline', 'backend-sonarqube-analysis.zip'), ('02-missing-coverage', 'backend-sonarqube-analysis (1).zip'), ('03-coverage-before-targeted-tests', 'backend-sonarqube-analysis (2).zip'), ('04-final-quality-gate-pass', 'backend-sonarqube-analysis (3).zip')]
EXPECTED_HASHES = {'01-pre-coverage-baseline': '6036cf223e51f49ca954967b107ec2e49ab7f45fa693de448963c0177bc63cd2', '02-missing-coverage': 'e3bae6df9b0cc848e2b95abb372c6fe8a27072273f0ebf497253c99ec11df17d', '03-coverage-before-targeted-tests': '833b1e965b4dc1e7cb94abfb512e35877ed938f0c5ba587fd0cfe500f2d5ed12', '04-final-quality-gate-pass': 'f35b014ff0353edd8de59d8b0455f37169c5fbca625fd68d77e14eb70462b6fd'}
XML_HASHES = {'final-run/coverage/ResearchTrack.AuthService.Tests/c4391454-24e0-4571-b2cf-be02fbef7dfc/coverage.opencover.xml': '45a005ccc0a4b24927db0b97cbc34f2fb09dc1fc9dda1e0fe5cdbdd209682e41', 'final-run/coverage/ResearchTrack.Gateway.Tests/e8960977-05e0-4182-9d43-ded7cd433009/coverage.opencover.xml': '18214bb6b77319d0c6909a1461ecd6f34845f95d38d19644dc6d5047a390b849', 'final-run/coverage/ResearchTrack.GitHubService.Tests/d226584b-594e-4cac-87ed-7541f56dd1bb/coverage.opencover.xml': 'a431d244a7284bb6e13004cc1b45c55509c15369f7889e72b509862f7b2eb16e', 'final-run/coverage/ResearchTrack.JiraService.Tests/25bc6f1d-459c-470e-843e-c96fe198ba23/coverage.opencover.xml': '460072fd9d5c508612c300f9726c41721c977871f9958a5d5cb85beeb21cf533', 'final-run/coverage/ResearchTrack.MeetingService.Tests/e878c331-a3af-4ca0-8406-757b76f75a51/coverage.opencover.xml': '1a38d03cd8c3d118639bdc6110bf438aae1a8b738912607380586254e9e9483c', 'final-run/coverage/ResearchTrack.ProjectService.Tests/0e920fb6-4cde-4cab-961d-a0f38b9d5091/coverage.opencover.xml': 'c4aa15dd2695d9d2e7d3613012dcc5d97c0454fc074e9f83fa651b014328c842', 'final-run/coverage/ResearchTrack.SubmissionService.Tests/b05d9ffc-8a2b-4580-b0be-8dc76c7e1aa2/coverage.opencover.xml': '969f09e8f4e42c074bbab013b3e8f649378e0583c1bb34e0afc8af20ba71f215'}
EXPECTED_FINAL_ID = 'a2ec6507-83b5-429d-bb4e-5c8831f70c86'


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def run():
    for stage, _original_name in SOURCES:
        zip_path = ROOT / 'source-artifacts' / f'{stage}.zip'
        check(zip_path.is_file(), f'Original ZIP missing: {zip_path}')
        check(digest(zip_path) == EXPECTED_HASHES[stage], f'SHA-256 mismatch: {zip_path}')
        with ZipFile(zip_path) as z:
            check(z.testzip() is None, f'Corrupt ZIP: {zip_path}')
            history = ROOT / 'history' / stage
            for filename in ('ce-task.json', 'quality-gate.json', 'measures.json', 'sonarqube-summary.md'):
                check((history / filename).read_bytes() == z.read(filename), f'Derived history differs: {stage}/{filename}')
            if stage.startswith('04-'):
                for info in z.infolist():
                    if info.is_dir():
                        continue
                    rel=Path(info.filename)
                    check('..' not in rel.parts and not rel.is_absolute(), f'Unsafe final path: {rel}')
                    extracted=ROOT/'final-run'/rel
                    check(extracted.is_file() and extracted.read_bytes()==z.read(info.filename), f'Final extraction differs: {info.filename}')
    final=ROOT/'final-run'
    ce=json.loads((final/'ce-task.json').read_text(encoding='utf-8'))['task']
    gate=json.loads((final/'quality-gate.json').read_text(encoding='utf-8'))['projectStatus']
    ms=json.loads((final/'measures.json').read_text(encoding='utf-8'))['component']['measures']
    measures={v['metric']:v for v in ms}
    check(ce['status']=='SUCCESS' and ce['analysisId']==EXPECTED_FINAL_ID, 'Final compute engine/analysis ID not verified')
    check(ce['branch']=='main', 'Final branch not main')
    check(gate['status']=='OK' and gate['ignoredConditions'] is False, 'Final cloud gate not a genuine OK')
    check(len(gate['conditions'])==6 and all(c['status']=='OK' for c in gate['conditions']), 'Not all six conditions passed')
    new_cov=next(c for c in gate['conditions'] if c['metricKey']=='new_coverage')
    check(float(new_cov['actualValue'])>=80 and float(new_cov['errorThreshold'])==80, 'New-code coverage threshold invalid')
    check(float(measures['coverage']['value'])==60.2, 'Unexpected overall coverage metric')
    check(int(measures['ncloc']['value'])==27006, 'Unexpected LOC metric')
    xml_files=sorted(final.glob('coverage/**/*.opencover.xml'))
    check(len(xml_files)==7, f'Expected seven final OpenCover files, found {len(xml_files)}')
    for f in xml_files:
        rel=f.relative_to(ROOT).as_posix()
        check(digest(f)==XML_HASHES[rel], f'OpenCover SHA-256 mismatch: {rel}')
        root=ET.parse(f).getroot()
        check(root.tag=='CoverageSession' and root.find('Summary') is not None, f'OpenCover invalid: {rel}')
    print('PASS — 4 byte-identical GitHub artifact archives; historical JSON intact')
    print('PASS — final SonarQube CE SUCCESS; 6/6 gate conditions OK; new coverage 96.7%')
    print('PASS — 7 authentic OpenCover XML reports with SHA-256 verification')
    print('NOTE — this validates archived evidence; it does not execute .NET tests or check GitHub environment enforcement')


if __name__ == '__main__':
    try:
        run()
    except (AssertionError, OSError, ValueError, KeyError, ET.ParseError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        sys.exit(1)
