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


# Pages

1. Main page?? Do I need? [ok] // HomePage
2. MenuView
    - user
        - profile
        - logout
    - test
    - testplan
3. Test listing page [ok]
4. Test details page [ok]
5. Create Test page
6. Riport view
7. Test Plan Listing Page
8. Test plan details page
9. Merged Riport View