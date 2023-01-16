# Python3 code to find frequency of each word
# function for calculating the frequency
def freq(str):
    # break the string into list of words
    str_list = str.split()

    # gives set of unique words
    unique_words = set(str_list)

    for words in unique_words:
        print('Frequency of ', words, ':', str_list.count(words))


# driver code
if __name__ == "__main__":
    str = 'In its most abstract sense, an ecosystem is a biotic community, encompassing its physical environment, and all the interactions possible in the complex of living and nonliving components. Economics has always been about systems that explain differential output and outcomes. However, economics has generally ignored the role of entrepreneurship in economic systems, just as entrepreneurship studies have largely overlooked the role of systems in explaining the prevalence and performance of entrepreneurship. The entrepreneurial ecosystem approach has the promise to correct these shortcomings. Its two dominant lineages are the regional development literature and the strategy literature. Both lineages share common roots in ecological systems thinking, providing fresh insights into the interdependence of actors in a particular community to create new value. But studies of both regional development and strategic management have largely ignored the role of entrepreneurs in new value creation. In this paper, we will outline contributions to the entrepreneurial ecosystem approach and conclude with a promising new line of research to our understanding of the emergence, growth, and context of start-ups that have achieved great impact by developing new platforms. © 2017, Springer Science+Business Media New York.'

    # calling the freq function
    freq(str)
