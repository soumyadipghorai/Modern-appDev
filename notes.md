### components 
* storage 
* computation 
* presentation

### platforms 
* desktop
* webbased 
* mobile 
* embedded -> single function, limited scope --> watch

### Architecture 
* client server 
* distributed- peer to peer 

### design pattern
MVC --> model view controller 
  
**model :** store emails on server, index, ready to manipulate 

**view :** display list of emails, read indv emails 

**controller :** sort emails, delete, archive 

### UI design 

UI 
--> screen, audio, vibration, motor 

--> key/ mouse, touch, button 

types of views 
1. fully static --> google home 
2. partly dynamic --> wiki pedia 
3. mostly dynamic --> amazon 

output 
1. HTML 
2. dynamic image 
3. Json/XML - machine readable 

UI design :

* goal 
1. simple - easy for user to understand 
2. efficient - user achieves goal with minimal effort 

* aesthetics 
* accessibility - by everyone (with some disability)


Systematic Process 
1. functionality requirements -> what is needed 
2. user and task analysis -> user preferences, task needed 
3. prototype -> wireframes, mockups 
4. testing after deployment -> user acceptance, usability 


Heuristics ([Jakob Nielsen's heuristics for design](https://www.nngroup.com/articles/ten-usability-heuristics/))

General principles : 
1. consistency 
2. simple and minimal steps 
3. Simple language 
4. Minimal and aesthetically pleasing 


Tools :
* Wireframes (lucidchart)
1. visual guide to represent structure of web page 
2. info design 
3. navigation design 
4. UI design  

template engine -> jinja2

* Accessibility 
**standard**

interplay between many components of a page 
1. web content - HTML, images
2. user-agent: desktop browser, mobile browser, speech oriented browser 
3. authoring tool: text editor, compiler  

**perceivable** 
1. text alt 
2. captions and other alt
3. make it easier for users to see and hear content 

**operable** 
1. keyboard 
2. enough time 
3. inputs other than keyboard 
4. don't use content that causes seizures 
5. help users navigate and find content 

**Understandable** 
1. readable and understandable 
2. avoid and correct mistakes -> input int 
3. predictable 

**robust** 
1. compatibility 