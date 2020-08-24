# site-text-hunter
A simple web scrapping tool with Scrapy lib embedded into a python script. 

To use it, follow the steps below:
 - Install the current version of python in your machine.
 - Open your terminal and check if python is installed by typing "py". If the command fails, remember to add python to the environment variables. Then, check again.
 - After check if "py" command is working, open another terminal window and install the following libraries: scrapy, pandas and bs4, using the following command:
   "py -m pip install pandas bs4 Scrapy logging" (recommended for Windows OS) or "pip install pandas bs4 Scrapy logging" (recommended for Linux and MacOS environments)
 - With the installed libraries, clone the repository into your desired path.
 - Open the code.
 - First step, you need to choose what URL's you would like to scrap, add them to:
    start_urls = [''' ADD THE URL OF THE SITE HERE '''] at line 27.
 - Second step, you should fill the domain of the site you added before, at this part:
    allowed_domains = [''' ADD THE DOMAIN OF THE SITE HERE '''] at line 26.
 - Third step, inspect you url, by access it and press, with the right button of your mouse, the option "inspect" the text you want to catch, fill the name of the style 
   attribute that the site uses and the value of the style attribute and them to this part:
     conteudo_do_site = soup.findAll('[ADD_THE_TAG_THAT_COVERS_THE_ENTIRE_TEXT]', {'[ADD_THE_STYLE_ATTRIBUTE_NAME]': '[ADD_THE_STYLE_ATTRIBUTE_VALUE]'})
 - Example: 
     .For the given URL: https://www.nytimes.com/2020/08/24/world/covid-19-coronavirus.html?action=click&module=Top%20Stories&pgtype=Homepage
     .Open it.
     .Inspect the text you want to catch by click on it with right button and pressing "Inspect" or "Inspecionar".
     .Find the HTML tag that covers all the text you want, in this case is: <div class="css-53u6y8">
     .For this code: conteudo_do_site = soup.findAll('[ADD_THE_TAG_THAT_COVERS_THE_ENTIRE_TEXT]', {'[ADD_THE_STYLE_ATTRIBUTE_NAME]': '[ADD_THE_STYLE_ATTRIBUTE_VALUE]'})
      [ADD_THE_TAG_THAT_COVERS_THE_ENTIRE_TEXT] will be equals to 'div',
      [ADD_THE_STYLE_ATTRIBUTE_NAME] will be equals to 'class',
      [ADD_THE_STYLE_ATTRIBUTE_VALUE] will be equals to 'css-53u6y8'
     .The final result will be: conteudo_do_site = soup.findAll('div', {'class': 'css-53u6y8'})
  - Finally, open the terminal in the path of the project and run: py hunter.py
  - The desired text will be printed.
  
  OBS: The exited evolutions of the code will be commited.
       
