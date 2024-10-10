import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    n=len(corpus)
    d={i:(1-damping_factor)/n for i in corpus}
    if corpus[page]:
        k=damping_factor/len(corpus[page])
        for j in corpus[page]:
            d[j]+=k
    # else:
    #     for i in corpus:
    #         d[i]+=damping_factor/n
    return d

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    c={page : 0 for page in corpus}
    c_p = random.choice(list(corpus.keys()))
    for i in range(n):
        c[c_p]+=1/n
        p=transition_model(corpus,c_p,damping_factor)
        c_p=random.choices(population=list(corpus.keys()),weights=[p[l] for l in corpus],k=1)[0]
    return c

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    n=len(corpus)
    # print(corpus)
    c={i:1/n for i in corpus}


    while True:
        n_p=dict()
        for page in corpus:
            n_rank=(1-damping_factor)/n
            s=0
            for i in corpus:
                if page in corpus[i]:
                    s+=c[i]/len(corpus[i])
                if not corpus[i]:
                    s+=c[i]/n
            s=damping_factor*s
            n_p[page]=n_rank+s
        if all(abs(n_p[page]-c[page])<0.001 for page in c):
            break
        c=n_p
    return c





if __name__ == "__main__":
    main()
