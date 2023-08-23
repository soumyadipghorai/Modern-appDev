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

8bits - ASCII
UCS-2 - 2byte 
UCS-4 4 byte

5000 character doc --> 
UCS-4 --> 32b*5000 = 160000 bits
ASCII --> 8b * 5000 = 40k 
original 7bit --> 7b * 5000 = 35k


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

network simulation and page simulation 

**persistent storage**
if we use python datastructures to store the data might get lost after we stop the server, but we need to retrive the info, we can use csv or tsv to handle this. but it has its own limitations so we move to databases. 

NOSQL databases because of the structure might be slower at times to process the querries than the SQL databases. 

### Relationship types : 

1. One-to-one -> student has one roll number, one roll number uniquely identifies one student.
2. one-to-many (many-to-one) -> one student can live in one hostel but many student can live in one hostel, save email in folders. one email in one folder but one folder has many email.
3. many-to-many -> one student can register into many courses, one course can have many students. 

**Diagrams :**
1. ERD 
2. UML 
3. class relation

A -||---|| B        one-to-one
A -||--o<- B        one-to-many
A --<- B            one-to-many (crow's feet)

-||---o<- 
one order must have exactly one customer --> ne custimer may have 0 or many orders 

### controller

Model---updates---->view <br>
 |                     |<br>
manipulate___________sees <br>
 |                     |<br>
controller-<--uses--User<br>

basic request : clicking on link/ url --> GET 
more complex : form submission -> POST 

**CRUD** (create read delete update) <br>
**API** (Application programming interface) <br>
some standard way to communicate with a server. it doesn't matter for the client if the database is made in mysql or pgsql as long as I can make a request and server returns what I want. CRUD is considered the 1st level api.

### Laravel PHP framework
<table>
    <thead>
        <tr>
            <td>verb</td>
            <td>url</td>
            <td>action</td>
            <td>route namecontroller</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>GET</td>
            <td>/photos</td>
            <td>index</td>
            <td>photos.index</td>
        </tr>
        <tr>
            <td>GET</td>
            <td>/photos/create</td>
            <td>create</td>
            <td>photos.create</td>
        </tr>
        <tr>
            <td>POST</td>
            <td>/photos</td>
            <td>store</td>
            <td>photos.store</td>
        </tr>
        <tr>
            <td>GET</td>
            <td>/photos/{photo}</td>
            <td>show</td>
            <td>photos.show</td>
        </tr>
        <tr>
            <td>GET</td>
            <td>/photos/{photo}/edit</td>
            <td>edit</td>
            <td>photos.edit</td>
        </tr>
        <tr>
            <td>PUT/PATCH</td>
            <td>/photos/{photo}</td>
            <td>update</td>
            <td>photos.update</td>
        </tr>
        <tr>
            <td>DELETE</td>
            <td>/photos/{photo}</td>
            <td>destroy</td>
            <td>photos.destroy</td>
        </tr>
    </tbody>
</table>

**Rules of thumb** <br>
* should be possbile to change views without the model ever knowing (change screen from mobile to desktop but the backend should not know about it) <br>
* should be possible to change underlying storage of model without views ever knowing (the frontend should not know if I have changed my DB from sql to nosql [ORN SQLAlchemy]) <br>
* controllers/ actions should generally NEVER talk to a database directly (don't write SQL querry in the controller)

In practice voews and controllers tend to be more closely interlinked than with models

<!-- ### routes   -->

**REST and APIs**

REST - REpresentational State Transfer (software architecture)

constraint 1: client - server <br>
    server stores the data --> connects over the network to various clients 

constraint 2: stateless <br>
    server can't assume the state of the client or the server 

constraint 3: layered system <br>
    in between client and server there might be load balancers (front end to the server)<br>
    auth server --> authenticate the user <br>
    pool of backends --> real computation happens here. And the client need not know from where the response came 

constraint 4: cacheability <br>
    respnse directly from proxy cache without going to backend. Can data be stored in the cache memory 

constraint 5: Uniform interface <br>
    client and server are expected to interact in a uniform and predictable manner 

constraint 6: Code on demand <br>
    server can extend client functionality -> js, java applets 

**Sequence** <br>
URI -> uniform resource indentifier <br>
URL -> uniform resource locator <br>
URI > URL <br>

client access a resource indentifier -> resource operation specified as part f access [GET, POST] -> server responds with new resource indentifier 

GET -> Retrieve representation of target resource's state <br>
POST -> Enclose data in request<br>
PUT -> create a target resource with data enclosed<br>
DELETE -> delete the target resource<br>

idempotent -> GET, PUT, DELETE <br>
POST -> not 

**API** <br>
input -> text HTTP <br>
output -> complex data types --> JSON, XML, YAML 

different from internval server representation 
different from final view presentation 

YAML -> yet another markup language -> common alt, esp for documentation and configuration 

q(required) = search terms <br>
limit = max num of search results to return b/w 1-100, default 50 

respose

```
200 --> success, result found/ no result found 
400 --> query param not set / invalid limit requested 
500 --> search error 
```

**OpenAPI specification (OAS)**

```
openapi: 3.1.0
info: 
    title: A minimal OpenAPI document
    version: 0.0.1
paths: {} # No endpoints defined
```

Paths
```
openapi: 3.1.0
info: 
    title: Tic Tac Toe
    description: |
        This API allows writing down marks on a Tic Tac Toe board 
        and requesting the state of the board or of individual squares.
    version: 1.0.0
paths:
    /board:
```

Operation object
```
paths: 
    /board: 
        get: 
            summary: Get the whole board 
            description: Retrieves the current state of the board and the winner. 
            parameters: 
                ...
            responses:
                "200": 
                    description: Everythin went fine 
                    content: 
                        application/json: 
                            schema: 
                                type: integer
                                minimum: 1
                                maximum: 100
                        text/html: 
                            ... 
                        text/*: 
                            ...
```

```
application/json: 
    schema: 
        type: object
        properties: 
        productName:
            type: string 
        productPrice: 
            type: number 
``` 

**Best practice:**
1. design first vs code-first 
2. single source of truth 
3. source code version control 
4. OpenAPI is open- public dcumentation better to identify problems 
5. Automated tools, editors- make use of them!

```
types of storage: 
On-chip register: 10s-100s of bytes 
SRAM(cache): 0.1 - 1MB (static RAM)
DRAM : 0.1 - 10GB (dynamic RAM)
SSD - Flash: 1- 100GB 
Magnetic disk (HDD): 0.1 - 10 TB 
Optical, magnetic, holographic,...
```

latency : <br>
regster < SRAM < DRAM < SSD < HDD<br>
1st --> slow 

throughput : num of bytes/second that can be read (higher is better)<br>
DRAM > SSD > HDD 

Density: number of bits stored per unit area/cost (higher is better)<br>
HDD > SSD > DRAM > SRAM > Regs 

cold storage: amazon glacier, google, azure <br>
* high latency or retrieval: upto 48hours 
* very high durability and very low cost 

**Data Scearch:**

O(1) --> constant time independent of input size <br>
O(logN) --> log in input size <br>
O(N) --> linear in input size <br>
O(N^k) --> polynomial in input size <br>
O(k^N) --> exponential in input size <br>

linear search < binary search (sorted)

binary search tree (alter native) --> problem self-balancing

hash table --> compute an index for an element: O(1)

**search in a database:** 

stored in tables with column --> maintain index of columns to search on 

**hash index :**
1. only used in in-memory tables 
2. only for equality comparisons not for range
3. doesn't help with order by 
4. partial key prefix can't be used 
5. very fast where applicable

Document database: <br>
json file --> mongoDB, amazon documentDB 

key-value: <br>
python dict --> redis, berkeleyDB <br>
good for lookup not for range 

column store: <br>
traditional relationalDB --> cassandra, HBase 

graphs: <br>
friend of a friend --> Neo4j, amazon neptune 

time series database: <br>
application specific, used for log analysis, performance analysis --> RRDTool, InfluzDB, Prometheus <br>
search --> elasticsearch, graphana 

NoSQL --> not only SQL 

ACID: <br>
transactio: core principle of database <br>
atomic --> either entire row is created or left unchanged 
consistent --> 2 copies of database will have exact same values 
isolated --> one transaction should not interfare b/w another transaction
durable --> saved in storage 

why not ACID? 
* consistency is hard to meet --> eventual consistency is easier to meet 
* **financial transactions** absolutely require ACID 

data store 
--> in-memory (fast, doesn't scale across machine)
--> disk (different data structure)

**redundancy** --> multiple copies of same data, often used in connection with backups, one copy is still the master <br>
**replication** --> usually in context of performance, live replication requires careful design 

**BASE (basically available softsate eventual consistent)** --> stress on availability

replication possible in RDBMS --> geographically distributed replication harder 

scale up(tradtional) --> more RAM, faster network, requires machine restart 
scale-out --> multiple servers, harder to enforce consistency, better suited cloud models, auto scale up 

application specific --> financial transaction --> rdbms 
cloud --> social network 

```
name = form.request['name']
pswd = form.request['pswd']

sql = "SELECT * FROM Users WHERE name = '"+name+"' AND Pass = '"+ pswd + "'"

# fishy
name = " OR ""="
pswd = " OR ""="
SELECT * FROM Users WHERE Name = "" OR "" AND Pass = "" OR "";

# result is all the users from the database 

name = a; DROP TABLE Users; 

SELECT * FROM Users WHERE Name = a; DROP TABLE Users; 

# destroy all your data 
```
that's we need to do all the validation

SQL injection --> use known frameworks, best practices and validation 


**https(secure sockets)** --> in http a third party can tap in b/w and see all the communication b/w server and client. https makes it impossible to tap in b/w.

only secures link for data transfer but doesn't perform validation check. <br>
negative impact on caching of resources like static files. <br>
some overhead on performance.

static--> all pages on site are statically generated, compiled ahead of time

runtime HTML generation : <br>
traditional CGI/ WSGI based apps --> flask, django, ruby 

static pages --> apache ~ 10k req/s - 512 parallel requests 
Nginx ~20k req/s - 512 parallel requests 

**Asynchronous update** <br>
AJAX (Asynchronous js and xml) <br>

brython --> run python inside browser <br>
transpilation --> translation - compilation 

WASM --> Web assembly  

sandbox --> secure area that JS engine has access to 


#### Types of access : 
* read-only 
* read-write(CRUD)
* modify but not create 

#### Discretionary vs mandatory: 
* Discretionary --> you have control over who you share with, forwarding emails, changing files access modes etc 
* mandatory --> decisions made by centralized management - users can't even share info without permission, typically in military or high security scenarios. 

#### Principle of least privilege :
entity should have minimal access required to do the job 

benefits: 
* better security: 
* better stability 
* ease of deployment   

#### Types of security checks 
* obscurity (generally very bad idea) --> application listens on non-standard port known only to specific people. 
* address --> where are you coming from 
* login --> username/password 
* tokens --> access tokens that are difficult/impossible to duplicate, can be used for machine-to-machine authentication without password. 

`
401 - unauthorized 
404 - not found 
403 - forbidden 
`
