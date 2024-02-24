# Diploma work

### Django data models:
#### User
- name
- email
- password
- role
- createdAt
- deletedAt

#### Test
- name
- type (cypress/other)
- implementation (path to implementation file stored in server)
- createdBy (userID)
- createdAt
- deletedAt

#### TestPlan
- runAt
- createdBy (userID)
- createdAt
- deletedAt

#### Contains
- testID
- testPlanID

#### TestPlanExecution
- testPlanID
- createdAt
- deletedAt

#### Execution
- testID
- testPlanExecutionID
- status
- createdAt
- bugs
- executionTime
- reference
- info

#### Images
- executionID
- name
- filepath
