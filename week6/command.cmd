curl "https://en.wikipedia.org/w/rest.php/v1/search/page?q=earth&limit=1"
@REM call API and search for earth

curl "https://en.wikipedia.org/w/rest.php/v1/page/Main_Page/history" 
@REM history for main page 

curl -X GET "https://cdn-api.co-vin.in/api/vw/appointment/sessions/public/findByPin" -H "accept: application/json" -H "accept-Language: en_US"
@REM request json output and english output 

curl -X GET "https://cdn-api.co-vin.in/api/vw/appointment/sessions/public/findByPin?pincode=019283&date=04-08-2021" -H "accept: application/json" -H "accept-Language: en_US" -H "User-Agent: Mozilla/5.0"
@REM including pincode and date 

