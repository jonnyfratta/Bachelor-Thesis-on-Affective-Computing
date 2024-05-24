
# Affective Computing Thesis

This is the thesis i presented for my Bachelor's degree in Computer Enginering. 

## Usage/Examples
In the project there are two types of script:
- Histogram plot making
- Apriori Algorithm application

### Histogram plot making
These scripts allowed me to visualize the distribution of people in my dataset among the different age intervals I was testing.

### Apriori Algorithm application
The three different application files, are used to look for association rules between age interval of belonging and mistake making in a specific emotion evaluation method (SAM, AS or Emoji)


## Development
The dataset I worked on was obtained by having people take a test in which they watched a video and afterwards they had to identify their emotion through three differents emotion evalutaion methoeds.
I developed the project using Pandas library to handle the data stored in my dataset and the Mlxtend library to apply the Apriori algorithm and associations rule searching.

In the utility.py file, I associated to every video a "correct expected emotion" and then I associated to every emotion an interval of correct values in the different evaluation methods.

Since I was looking for niche rules, I applied the Apriori Algorithm with a minimum support of 1% and a minimum confidence value of 98%.


## Authors

- [@jonnyfratta](https://github.com/jonnyfratta)
