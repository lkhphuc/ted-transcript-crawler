# ted-transcript-crawler
A crawler to automatically download all the transcript of TED talks.
This crawler was built using Scrapy based on this tutorial https://blakeboswell.github.io/2016/scrapy-tedtalk/ but have modified it to be usable with the latest version of TED Website.

### To run: 
1. Install Scrapy
2. Download or clone the repo
3. run `cd ted-transcript-crawler/ted`
4. run `scrapy crawl ted_crawl`

### Output:
Outputs are stripped off all the html elements and contains only plaintext and whitespace. 
The outputs are saved in Json-line format.
