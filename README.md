# rate-meal
# note
Backend App-----> API -----> frontend
                     ------> mobile app

DataBase ----> models ------> views ----> context(dtl) X
                                    ---->API (endpoint)
                                    ---->Json Format
django high ----> python high 
                -----> problems Hacker rank



# MOdels (Design DataBase)

1 - Model ----> Meal
2 - Model ----> Review
3 - Model ----> User django

# serializer 
    ---> serialize --- data model to front
    --->deserialize --> enter data from front to model
# steps
1- http://127.0.0.1:8000/api/meals/meal_pk/rate_meal  ==> POST
   request data = stars 
   request user = user or user name 
   stars + user from request 
   pk from url 

   endpoint to update\create rate for specific meal using Meal vieset not rate 
   views > add the custom function with @action decarator