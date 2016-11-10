# Improving web search results by incorporating User Feedback
##### Term project for the course Information Retrieval 

PageRank plays an important role in deciding the relevance among the documents similar to the search query. While PageRank performs excellent in exploring the intrinsic structure of the WWW, the classic retrieval system does not incorporate any info on the popularity of the page and favoritism among the users. 

Tapping the User Feedback on a set of results can, hence, be used as a rich set of information for improving upon the quality of the search results..  

The project incorporates user click-through information into an existing ranking system to improve results based on the data received from previous instances when the pages on similar query is served to a User. This is done by maintaining a score of each page in the collection by means of Elo rating, a classical rating system for rating players in Chess, Tennis etc. The score of the page is increased when a link (out of many served) gets clicked, while that of others is reduced. Also, the change in score is in proportion to the position in which the page appears by the present state of the ranking system.  

More information on implementation is given in the documentation.

### # modules of the project include :
- **crawling and scraping** : implemented in python, uses multi-threading for running simultaneous connections to web. Uses BeautifulSoup for scraping text.
* **Indexing** : Implemented in C++ for running efficiency over the corpus of scraped text. Implements usual pre-processing techniques of Information Retrieval for generating tokens such as stopword removal, normalization, HTML decoding, Stemming.
* **PageRank** : Implemented in python. Calculates the PageRank score of pages in the collection by recursively iterating till the error in the PageRank matrix is reduced to the order of -6.
- **Elo Rating** : Implements Elo rating for each page. The ratings get updated each time the User clicks on the search results served to him. 
- **Rank Merging** : Merging the the ranks obtained from 3 sources viz. Similarity with the query, PageRank, Elo based on the calculated weights. Weights are calculated depending upon the confidence of the Elo Ratings, i.e. initially Elo Rating of all pages are the same, hence no significant contribution, but as the Elo Ratings get updated multiple number of times, it is given significant contribution in determining the final rankings. The weightage of other rankings (similarity and PageRank) is likewise adjusted.
- **GUI** : Implemented in Django 1.10.

### # working stats :
- 106,000 Wikipedia pages crawled, 1.4 M links extracted (~1 M unique)
- Size of raw data : 13.1 GB, Size of clean data : 1.7 GB
- 26 M edges in 1.4 M links 
- 14.3 M edges in 100,000 crawled pages
- ~2 M unique words in index
- total size of postings : 456 MB
- total number of tokens in all documents : ~73 M

### # made with passion by an awesome team :)
- Varun Vasudevan, Akshit Bhatia, Neel Kasat, and, me ! at BITS Pilani.