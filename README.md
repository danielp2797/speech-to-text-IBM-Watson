# Recaptcha bypass module with Natural Language Processing (powered with IBM Watson)

_In this project a basic speech to text translation is implemented via API calls to IBM Waton Speech to Text Service. The functionality is tested against google ReCaptcha v2 converting audio challenges to text._

### Pre-requisites 📋
(It is assumed that you have Python installed)
_It is mandatory to get an IBM Lite tier account. Follow the next steps to get free tier access:_
1. From the IBM (IBM ID must be created) home page search

![Alt text](figures/service/STT_search.png?raw=true "Title")
2. Provision a Lite instance (500 minutes of audio processing for free) 

![Alt text](figures/service/STT_provisioning.png?raw=true "Title")

3. Get the service API credentials

![Alt text](figures/service/STT_IBM_credentials.png?raw=true "Title")

4. Store credentials as .json file in

```
config/creentials/credentials.json
```

with the following structure:
```
{
  "APIkey": "API key here",
  "URL": "URL here"
}
```

## Start 🚀

_Just clone the repository_

```
git clone https://github.com/danielp2797/Amazon-reviews-scrap-and-sentiment-analysis-with-IBM-Watson
```
then install src package from setup.py file in the project root directory
```
pip install -e .
```
and finally install requirements
```
pip install -r requirements.txt
```

## Usage 📦
_Just define the audio to text conversion. Some sample captchas are given in:_
```
conversion/audio
```

and run the main.py script with the audio path as first argument:
```
python3 main.py <path to audio>
```
If it worked, you will see the conversion in your console.

## Demonstration ⭐️
Let's do a demonstration bypassing the tedious Google Recaptcha v2!

First visit the demo page 

```
www.google.com/recaptcha/api2/demo
```
check the box and the challenge should appear as follows:

![Alt text](figures/sample/demo_home_page.png?raw=true "Title")
click the headphone button and download the .mp3 file as follows:
![Alt text](figures/sample/download_captcha.png?raw=true "Title")
![Alt text](figures/sample/download_page.png?raw=true "Title")

Save the audio in the conversion folder. In this sample case:

```
conversion/audio/audio_test.mp3
```

Then call main.py as follows:

```
python3 main.py "conversion/audio/audio_test.mp3"
```

If conversion is successful, you will see it in console:

![Alt text](figures/sample/main_result.png?raw=true "Title")

Finally, if we paste the result in the captacha textbox, magic is done:

![Alt text](figures/sample/paste_results.png?raw=true "Title")
![Alt text](figures/sample/done.png?raw=true "Title")

## I hope this help you 🎁

The skeleton of this project can be integrated in a bot service to solve web captchas when required or other tasks which require speech conversion to text.
