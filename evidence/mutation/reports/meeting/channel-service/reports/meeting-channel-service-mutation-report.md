# Mutation Testing Summary

| File                                                           | Score  | Killed | Survived | Timeout | No Coverage | Ignored | Compile Errors | Runtime Errors | Total Detected | Total Undetected | Total Mutants |
| -------------------------------------------------------------- | ------ | ------ | -------- | ------- | ----------- | ------- | -------------- | -------------- | -------------- | ---------------- | ------------- |
| Configuration\/MeetingOptions.cs                               | N\/A   | 0      | 0        | 0       | 0           | 0       | 0              | 0              | 0              | 0                | 0             |
| Contracts\/MeetingChannelContracts.cs                          | N\/A   | 0      | 0        | 0       | 0           | 0       | 0              | 0              | 0              | 0                | 0             |
| Contracts\/MeetingRecordContracts.cs                           | N\/A   | 0      | 0        | 0       | 0           | 0       | 0              | 0              | 0              | 0                | 0             |
| Controllers\/ProjectMeetingChannelsController.cs               | N\/A   | 0      | 0        | 0       | 0           | 16      | 2              | 0              | 0              | 0                | 18            |
| Controllers\/ProjectMeetingRecordsController.cs                | N\/A   | 0      | 0        | 0       | 0           | 16      | 2              | 0              | 0              | 0                | 18            |
| Domain\/MeetingChannel.cs                                      | N\/A   | 0      | 0        | 0       | 0           | 12      | 0              | 0              | 0              | 0                | 12            |
| Domain\/MeetingChannelConstants.cs                             | N\/A   | 0      | 0        | 0       | 0           | 6       | 0              | 0              | 0              | 0                | 6             |
| Domain\/MeetingRecord.cs                                       | N\/A   | 0      | 0        | 0       | 0           | 10      | 0              | 0              | 0              | 0                | 10            |
| Domain\/MeetingRecordConstants.cs                              | N\/A   | 0      | 0        | 0       | 0           | 0       | 0              | 0              | 0              | 0                | 0             |
| Extensions\/MeetingFeatureExtensions.cs                        | N\/A   | 0      | 0        | 0       | 0           | 36      | 2              | 0              | 0              | 0                | 38            |
| Features\/IMeetingChannelService.cs                            | N\/A   | 0      | 0        | 0       | 0           | 0       | 0              | 0              | 0              | 0                | 0             |
| Features\/IMeetingRecordService.cs                             | N\/A   | 0      | 0        | 0       | 0           | 0       | 0              | 0              | 0              | 0                | 0             |
| Features\/MeetingChannelService.cs                             | 71.05% | 54     | 22       | 0       | 0           | 21      | 4              | 0              | 54             | 22               | 101           |
| Features\/MeetingRecordService.cs                              | N\/A   | 0      | 0        | 0       | 0           | 94      | 2              | 0              | 0              | 0                | 96            |
| Infrastructure\/IProjectAuthorizationClient.cs                 | N\/A   | 0      | 0        | 0       | 0           | 0       | 0              | 0              | 0              | 0                | 0             |
| Infrastructure\/IUserProfileClient.cs                          | N\/A   | 0      | 0        | 0       | 0           | 0       | 0              | 0              | 0              | 0                | 0             |
| Infrastructure\/ProjectAuthorizationClient.cs                  | N\/A   | 0      | 0        | 0       | 0           | 22      | 24             | 0              | 0              | 0                | 46            |
| Infrastructure\/UserProfileClient.cs                           | N\/A   | 0      | 0        | 0       | 0           | 18      | 49             | 0              | 0              | 0                | 67            |
| Persistence\/Configurations\/MeetingChannelConfiguration.cs    | N\/A   | 0      | 0        | 0       | 0           | 25      | 0              | 0              | 0              | 0                | 25            |
| Persistence\/Configurations\/MeetingRecordConfiguration.cs     | N\/A   | 0      | 0        | 0       | 0           | 31      | 0              | 0              | 0              | 0                | 31            |
| Persistence\/IMeetingChannelRepository.cs                      | N\/A   | 0      | 0        | 0       | 0           | 0       | 0              | 0              | 0              | 0                | 0             |
| Persistence\/IMeetingRecordRepository.cs                       | N\/A   | 0      | 0        | 0       | 0           | 0       | 0              | 0              | 0              | 0                | 0             |
| Persistence\/MeetingChannelRepository.cs                       | N\/A   | 0      | 0        | 0       | 0           | 22      | 0              | 0              | 0              | 0                | 22            |
| Persistence\/MeetingDbContext.cs                               | N\/A   | 0      | 0        | 0       | 0           | 3       | 0              | 0              | 0              | 0                | 3             |
| Persistence\/MeetingDbContextFactory.cs                        | N\/A   | 0      | 0        | 0       | 0           | 3       | 0              | 0              | 0              | 0                | 3             |
| Persistence\/MeetingPersistenceExtensions.cs                   | N\/A   | 0      | 0        | 0       | 0           | 5       | 0              | 0              | 0              | 0                | 5             |
| Persistence\/MeetingRecordRepository.cs                        | N\/A   | 0      | 0        | 0       | 0           | 23      | 0              | 0              | 0              | 0                | 23            |
| Persistence\/Migrations\/20260816143908\_InitialCreate.cs      | N\/A   | 0      | 0        | 0       | 0           | 4       | 0              | 0              | 0              | 0                | 4             |
| Persistence\/Migrations\/20261003070000\_AddMeetingChannels.cs | N\/A   | 0      | 0        | 0       | 0           | 49      | 0              | 0              | 0              | 0                | 49            |
| Persistence\/Migrations\/20261003100000\_AddMeetingRecords.cs  | N\/A   | 0      | 0        | 0       | 0           | 62      | 0              | 0              | 0              | 0                | 62            |
| Program.cs                                                     | N\/A   | 0      | 0        | 0       | 0           | 11      | 0              | 0              | 0              | 0                | 11            |

## The final mutation score is 71.05%

### *Coverage Thresholds: high:80 low:65 break:65*
