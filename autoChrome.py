# pip install selenium

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome() # abre o browser Chrome no modo headless, sem interface grafica 
browser.get('http://www.python.org') # acessa a pagina do python

    # encontra o elemento que possui id=q e preenche com "selenium" (pode ser qualquer texto)
elem = browser.find_element_by_id("q")  # find the query box (the search box) and enter search term 'pycon' in it   <input type="text" name="q" value="" maxlength="255">   <input type="submit" value="Search Python">     <div class='result-count'>Results 1 to 10 of 22</div>      </form>     </li>    </ul>   </li>  </ul></div><!-- /search -->            <!-- main navigation -->   <nav role="navigation"><ul class='menu'><li><a href="/about/community/" title="" accesskey="#">Community</a></li><li class='current'><a href="/downloads/" title="" accesskey="#">Downloads</a></li><li><a href="/docs/" title="" accesskey="#">Documentation</a></li><!--<li class='last' ><a href="/support/" title="" accesskey="#">Support</a></li>--></ul></nav>        <!-- footer -->       <footer id='footer'>         &copy; 2001–2019 Python Software Foundation<br/>           Made with love by the Web community<br/>           Hosted by GitHub<br/>             To the extent permitted by law, the contributors to this site have waived all copyright and related or neighboring rights to this work.<br/          This work is published from: United States.</footer></body></html>"