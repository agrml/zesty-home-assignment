## How to run

1. Install the requirements: `pip install -r requirements.txt`
2. Set you credentials in settings.py
3. run `zesty/etl.py`
4. import `api.get_ec2_instances` to your shell or add a runner code to `zesty/api.py`:
```
    if __name__ == '__main__':
        print(get_ec2_instances('us-east-1'))
```


## Review notes

1. I've added `storage` directory to the repo, so you could review the script run result without actual cloning the repo. Ofcourse we don't store code run results in git in real life.
2. There were no requirements to write tests and add linters, so I didn't. In real life I would write a few pytest test, run black auto-formatting and add flake8 with some plugins in order to keep future development smooth. 
3. "What happens if things go wrong and code crashes?"
   1. Well, we should handle errors in `get_ec2_instances`. But in which way? 
   2. As I understood by fast googling, boto3 performs retries itself, so we don't need to code any retry logic
   3. If there are Access error, Server error or retries did not help, we should log the error and keep going in a decided way. Which way should we choose in this smple task? I have no information for it. Aborting with an exception which will be automatically logged seems fine to me.
4. "Your code should be as simple as possible, yet well documented and robust."
   1. I find this code self-documented thanks to dividing into short functions, dividing into well-named modules and using type annotations.

So thanks for the task, I hope for further communication.
