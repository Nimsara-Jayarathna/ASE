# Mutation Testing Summary

| File                                                                    | Score  | Killed | Survived | Timeout | No Coverage | Ignored | Compile Errors | Runtime Errors | Total Detected | Total Undetected | Total Mutants |
| ----------------------------------------------------------------------- | ------ | ------ | -------- | ------- | ----------- | ------- | -------------- | -------------- | -------------- | ---------------- | ------------- |
| Configuration\/StorageOptions.cs                                        | N\/A   | 0      | 0        | 0       | 0           | 4       | 0              | 0              | 0              | 0                | 4             |
| Configuration\/SubmissionOptions.cs                                     | N\/A   | 0      | 0        | 0       | 0           | 4       | 0              | 0              | 0              | 0                | 4             |
| Contracts\/SubmissionContracts.cs                                       | N\/A   | 0      | 0        | 0       | 0           | 0       | 0              | 0              | 0              | 0                | 0             |
| Controllers\/ProjectSubmissionsController.cs                            | N\/A   | 0      | 0        | 0       | 0           | 6       | 2              | 0              | 0              | 0                | 8             |
| Controllers\/SubmissionRequirementsController.cs                        | N\/A   | 0      | 0        | 0       | 0           | 6       | 2              | 0              | 0              | 0                | 8             |
| Domain\/ResearchSubmission.cs                                           | N\/A   | 0      | 0        | 0       | 0           | 0       | 0              | 0              | 0              | 0                | 0             |
| Domain\/SubmissionConstants.cs                                          | N\/A   | 0      | 0        | 0       | 0           | 4       | 3              | 0              | 0              | 0                | 7             |
| Domain\/SubmissionRequirement.cs                                        | N\/A   | 0      | 0        | 0       | 0           | 3       | 0              | 0              | 0              | 0                | 3             |
| Domain\/SubmissionReview.cs                                             | N\/A   | 0      | 0        | 0       | 0           | 2       | 0              | 0              | 0              | 0                | 2             |
| Domain\/SubmissionUploadSession.cs                                      | N\/A   | 0      | 0        | 0       | 0           | 7       | 0              | 0              | 0              | 0                | 7             |
| Domain\/SubmissionVersion.cs                                            | N\/A   | 0      | 0        | 0       | 0           | 5       | 0              | 0              | 0              | 0                | 5             |
| Extensions\/SubmissionFeatureExtensions.cs                              | N\/A   | 0      | 0        | 0       | 0           | 107     | 2              | 0              | 0              | 0                | 109           |
| Features\/ExpiredUploadSessionCleanupService.cs                         | N\/A   | 0      | 0        | 0       | 0           | 27      | 2              | 0              | 0              | 0                | 29            |
| Features\/IResearchSubmissionService.cs                                 | N\/A   | 0      | 0        | 0       | 0           | 0       | 0              | 0              | 0              | 0                | 0             |
| Features\/ISubmissionRequirementService.cs                              | N\/A   | 0      | 0        | 0       | 0           | 0       | 0              | 0              | 0              | 0                | 0             |
| Features\/ResearchSubmissionService.cs                                  | 60.42% | 203    | 133      | 0       | 0           | 27      | 12             | 0              | 203            | 133              | 375           |
| Features\/SubmissionFileRules.cs                                        | N\/A   | 0      | 0        | 0       | 0           | 36      | 2              | 0              | 0              | 0                | 38            |
| Features\/SubmissionRequirementService.cs                               | N\/A   | 0      | 0        | 0       | 0           | 155     | 7              | 0              | 0              | 0                | 162           |
| Features\/SubmissionResponsibilityRules.cs                              | N\/A   | 0      | 0        | 0       | 0           | 65      | 0              | 0              | 0              | 0                | 65            |
| Infrastructure\/IObjectStorageService.cs                                | N\/A   | 0      | 0        | 0       | 0           | 0       | 0              | 0              | 0              | 0                | 0             |
| Infrastructure\/IProjectAuthorizationClient.cs                          | N\/A   | 0      | 0        | 0       | 0           | 0       | 0              | 0              | 0              | 0                | 0             |
| Infrastructure\/IUserProfileClient.cs                                   | N\/A   | 0      | 0        | 0       | 0           | 0       | 0              | 0              | 0              | 0                | 0             |
| Infrastructure\/ProjectAuthorizationClient.cs                           | N\/A   | 0      | 0        | 0       | 0           | 48      | 69             | 0              | 0              | 0                | 117           |
| Infrastructure\/ProjectSubmissionContext.cs                             | N\/A   | 0      | 0        | 0       | 0           | 2       | 0              | 0              | 0              | 0                | 2             |
| Infrastructure\/S3ObjectStorageService.cs                               | N\/A   | 0      | 0        | 0       | 0           | 49      | 2              | 0              | 0              | 0                | 51            |
| Infrastructure\/UserProfileClient.cs                                    | N\/A   | 0      | 0        | 0       | 0           | 18      | 49             | 0              | 0              | 0                | 67            |
| Persistence\/Configurations\/ResearchSubmissionConfiguration.cs         | N\/A   | 0      | 0        | 0       | 0           | 27      | 0              | 0              | 0              | 0                | 27            |
| Persistence\/Configurations\/SubmissionRequirementConfiguration.cs      | N\/A   | 0      | 0        | 0       | 0           | 28      | 0              | 0              | 0              | 0                | 28            |
| Persistence\/Configurations\/SubmissionReviewConfiguration.cs           | N\/A   | 0      | 0        | 0       | 0           | 21      | 0              | 0              | 0              | 0                | 21            |
| Persistence\/Configurations\/SubmissionUploadSessionConfiguration.cs    | N\/A   | 0      | 0        | 0       | 0           | 37      | 0              | 0              | 0              | 0                | 37            |
| Persistence\/Configurations\/SubmissionVersionConfiguration.cs          | N\/A   | 0      | 0        | 0       | 0           | 25      | 0              | 0              | 0              | 0                | 25            |
| Persistence\/Migrations\/20260816143912\_InitialCreate.cs               | N\/A   | 0      | 0        | 0       | 0           | 4       | 0              | 0              | 0              | 0                | 4             |
| Persistence\/Migrations\/20261003210000\_AddSubmissionFoundation.cs     | N\/A   | 0      | 0        | 0       | 0           | 219     | 0              | 0              | 0              | 0                | 219           |
| Persistence\/Migrations\/20261004003000\_AddSubmissionReviewWorkflow.cs | N\/A   | 0      | 0        | 0       | 0           | 87      | 0              | 0              | 0              | 0                | 87            |
| Persistence\/Migrations\/20261004030000\_RemoveSubmissionComments.cs    | N\/A   | 0      | 0        | 0       | 0           | 44      | 0              | 0              | 0              | 0                | 44            |
| Persistence\/Migrations\/20261004093000\_AddSubmissionResponsibility.cs | N\/A   | 0      | 0        | 0       | 0           | 51      | 0              | 0              | 0              | 0                | 51            |
| Persistence\/SubmissionDbContext.cs                                     | N\/A   | 0      | 0        | 0       | 0           | 2       | 0              | 0              | 0              | 0                | 2             |
| Persistence\/SubmissionDbContextFactory.cs                              | N\/A   | 0      | 0        | 0       | 0           | 3       | 0              | 0              | 0              | 0                | 3             |
| Persistence\/SubmissionPersistenceExtensions.cs                         | N\/A   | 0      | 0        | 0       | 0           | 5       | 0              | 0              | 0              | 0                | 5             |
| Program.cs                                                              | N\/A   | 0      | 0        | 0       | 0           | 11      | 0              | 0              | 0              | 0                | 11            |
| Properties\/AssemblyInfo.cs                                             | N\/A   | 0      | 0        | 0       | 0           | 0       | 0              | 0              | 0              | 0                | 0             |

## The final mutation score is 60.42%

### *Coverage Thresholds: high:80 low:60 break:55*
