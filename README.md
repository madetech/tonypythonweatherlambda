# tonypythonweatherlambda

## Deployment instructions based on [link](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html)
1. Install libraries locally
```
pip install --target ./package requests
```
2. Zip up libraries
```
cd package && zip -r ../my-deployment-package.zip . && cd ..
```
3. Zip up lambda function
```
zip -g my-deployment-package.zip lambda_function.py
```
4. List zip file contents
```
unzip -l my-deployment-package.zip
```
5. Push lambda zip to AWS
```
aws-vault exec madesso -- aws lambda update-function-code --function-name getLondonWeather --zip-file fileb://my-deployment-package.zip
```
