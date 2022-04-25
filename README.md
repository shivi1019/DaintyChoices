Install node by downloading the appropriate version
`` https://nodejs.org/en/download/``
then install serverless
``npm install -g serverless``.

Then run ``npm init`` to initialize this for future npm packages. 

Finally you will need to install ``serverless-finch`` to ensure that the relevant html files in ``client/dist`` get uploaded. 
``npm install --save serverless-finch``
You may need ``sudo`` depending on how you installed npm. 

After this is set up, set your aws key and id (ask me for these offline) using
```
serverless config credentials --provider aws --key AWS_ACCESS_KEY --secret 
```


Deployment procedure
```
serverless deploy
serverless client deploy --no-delete-contents #without this it WILL delete contents
```

