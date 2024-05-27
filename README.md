# From Idea to Chatbot

### Setup your development environment:

|Task|URL  |
|--|--|
| Watch a quick video on dev environment setup | https://youtu.be/Zwgj9JdgM0U |
| Install Visual Studio Code (or you're favorite editor) | https://code.visualstudio.com/download |
| Install Python | https://www.python.org/downloads/ |

### Setup an OpenAI account and obtain an API Key

|Task|URL  |
|--|--|
| Watch a quick video on registering with OpenAI/Obtaining API Key | https://youtu.be/kALp2yN6fic |
| Create an OpenAI account | https://platform.openai.com/signup?launch |
| Create an OpenAI API Key | https://platform.openai.com/account/api-keys. |

<span style="background-color: #FFFF00">CRITICAL!!! Copy the key generated in these steps and store it somewhere safe - we will need this for activities during the lab!!!</span>

### Put it all together and verify it works

This last step is to ensure everything you have done so far is working as expected. In addition to a quick video, there we have pasted the code snippet as well as the pip command to install openai.

| Task | URL |
|--|--|
| Watch a quick video on testing out your dev environment and API Key | https://youtu.be/TjJS7C161II |

From the video: Installing OpenAI for use with Python:

```
pip install openai
```

From the video: ```demo.py``` in this repo (NOTE: replace \<YOUR API KEY GOES HERE> with your API Key)

From the video: TEST!!! by running the application
```
python demo.py
```
## STREAMLIT
Streamlit creates a web interface for your python code with a few lines of code. You could do it in your local or deploy it to streamlit public cloud.

### Run locally
`streamlit run therapist.py`

### Deploy to public cloud
1. Commit your code (remove API key line). 
2. Create `requirements.txt` and include all the module names (names only, import keyword not needed)
3. Create a streamlit account and tie it to your github. Go to https://streamlit.io
4. Create a new app -- Provide your github repo, branch, python file.
5. Choose a custom name of your app.
6. Click on Advanced Settings, go to SECRETS and provide OPENAI_API_KEY="your API key here"
7. Hit Deploy.
8. Your app should come up. If you face issues, ask ChatGPT.

## COMMON ISSUES
Here's a list of some common issues that you may come across. If you have any issues, please let us know and we'll add them to the list to help others out.

**Issue 1:**

 If you attempt to run the python demo.py and you get the following error:
 ```
 can't open file 'demo.py': [Errno 2] No such file or directory
 ```

Ensure you are in the same directory as the demo.py file - python can not find the file you are attempting to compile and run.

**Issue 2:**

If you get the following error:

```
Exception has occurred: ModuleNotFoundError
No module named 'openai'
```
You need to ensure that you ran the following command prior to attempting to compile and run:

```
pip install openai
```
**Issue 3:**

If you get the following error:

```
openai.error.AuthenticationError: Incorrect API key provided: <YOUR AP************ERE>. You can find your API key at https://platform.openai.com/account/api-keys.
```

You have either a bad API Key or you have not updated the code with your current API Key. To fix this, either overwrite the \<YOUR API KEY GOES HERE> section with your API Key, or go through the same process as getting a new API Key 
(https://platform.openai.com/account/api-keys)  and replace it.

**Issue 4:**

If you get the following error:

```
Command 'python' not found, did you mean:
```
* You need to check if python is installed --> ```python3 --version```
* If it installed, check if your symbolick link is setup as python3, try ```python3 demo.py```

**Issue 5:**

If you get the following error:

```
You exceeded your current quota, please check your plan and billing details 
```
* This EITHER means you have exhausted your $5 free credit that were allocated with free API account 
* OR you opened your account 90 days ago

* To fix - you need to get a paid account. Remember to set the max billing amount to a something like $5 or so. It is sufficient to last for months.

## Resources to further your learning
**Prompt Engineering Best Practices** 
https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api 

**AI for everyone by Andrew Ng**
https://www.coursera.org/learn/ai-for-everyone 

**ChatGPT Prompt Engineering for Developers** 
https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/

**Power of ChatGPT in your spreadsheets**
https://www.linkedin.com/pulse/get-power-chatgpt-your-spreadsheets-docs-allie-k-miller/ 

**AI for Good Specialization (applied learning)**
https://www.coursera.org/specializations/ai-for-good 

**Introduction to Generative AI (Google Cloud)**
https://www.cloudskillsboost.google/course_templates/536 
