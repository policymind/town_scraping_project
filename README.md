# PolicyMind Town Scraping

## Starting with document retrieval
While the ultimate goal of this project is to develop a local-policy retrieval-augmented generation (RAG) model, the first step (like all machine learning projects) is gathering our data. The embedding and LLMs are later steps.
![image](https://github.com/user-attachments/assets/71d1aa5a-4273-4a7e-9fa4-61f617ac8c58)

What this project offers TO YOU:
 - real Python experience
 - a shiny github portfolio example
 - experience with project feedback and questions (from me!)
 - evidence of collaboration in your GitHub profile
 - A chance to make a difference and contribute to more juicy stuff as we go forward!

## The task at hand:
[Massachusetts](https://www.mass.gov/info-details/massachusetts-city-and-town-ordinances-and-by-laws) provides links to the bylaws of towns across the state. The Massachusetts town codes are broken into three categories:
 - Regular bylaws (for example, no horse-drawn carriages are allowed to block the street for more than 3 minutes without fines)
 - Zoning (for example, this area is residential, and this area is for the pubs)
 - Other (for example, one town created a separate document for their dog laws)

We will target **regular** bylaws first, and we can incorporate other policy types later. The links to **regular** bylaws can be divided into four categories: hosted on [municode](https://www.civicplus.com/codification-software-services/), hosted on [ecode360](https://www.generalcode.com/library/), a URL that includes `.pdf`, and the remaining catch-all category I've labeled "crawl."

#### distribution of URL categories
| url_type | count |
| -------- | ----- |
| municode | 15    |
| ecode    | 130   |
| pdf      | 8     |
| crawl    | 189   |


## Goal: modular code
 Success criteria: A module for each scenario that accepts a `URL,` creates **one** file, saves file, and returns the path to the pdf file.

```
def municode(policy_url: str)-> path:
  """
  function to scrape all content from target municode link
  """

  
  return pdf_path
```
Each subdirectory of this repo contains:
 - fuller description of the task
 - data sample

## How to contribute! 
 - Fork this repo
 - create a branch `module_proposal`
 - Work on the module of your choice
 - Add me @aapebles as a collaborator for this repo!
 - When you're ready, create a pull request to your repo's main branch and add me as a reviewer. Within the pull request, include either:
   - A link to a jupyter notebook that neatly explains how you researched this and what you are proposing based on this research (this is what will stand out in your portfolio!)
   - Tables and images in the pull request body explain your reasoning, with links to where your analysis code is stored

## KEY QUESTIONS:
> How should multiple files(pdfs/html) be handled? combined? concatted?

If you think we're missing something, let me know! Use issues and discussions.


 ## Thank you for your interest!
![thank you](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeTRrbWh6dGxzbnN5YWc1djNuZmQ2bDB1Y2xlcHo0azVxY3N6NGZiMiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/26gsjCZpPolPr3sBy/giphy.gif)
![another thank you](https://media.giphy.com/media/QAsBwSjx9zVKoGp9nr/giphy.gif?cid=790b7611y4kmhztlsnsyag5v3nfd6l0uclepz4k5qcsz4fb2&ep=v1_gifs_search&rid=giphy.gif&ct=g)
![grover thank you](https://media.giphy.com/media/xdMXeiY2iCfSQ6faTk/giphy.gif?cid=790b7611y4kmhztlsnsyag5v3nfd6l0uclepz4k5qcsz4fb2&ep=v1_gifs_search&rid=giphy.gif&ct=g)
 
