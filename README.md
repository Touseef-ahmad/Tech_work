# Documentation written by Touseef Ahmad
# Tech_work
## Apps
This project contains 2 apps **users** and **work_diary**

## Users
this app has three main objectives 1) signup 2) signin 3) logout

## work_diary
this app has two main objectives add and delete working hours

## Working urls
Following are the urls and their function.
1) / : the home url user is redirected to login page if not logged in. supports both post and get request. user can add and view their working hours only
2) /users/login : both get and post requests . user view login page and can login
3) /users/register : both get and post requests . user view signup page and can signup
4) /users/logout : supports get request logs the user out
5) /delete/work_id/ : deletes the work entry 
