---
title: "Censorship of Online Encyclopedias: Implications for NLP Models"
author: "Chris Albon"
date: 2021-03-01T11:53:49-07:00
description: "Research notes on Yang and Roberts 2021"
type: technical_note
draft: true
---

## Summary

[Yang and Roberts 2021](https://arxiv.org/pdf/2101.09294.pdf) use word embeddings to show how the Chinese online encyclopedia Baidu Baike has censored concepts like democracy and collective action by comparing them to Chinese language Wikipedia.

## Notes

- **Wikipedia Blocked By China**
    - "Chinese language Wikipedia has been blocked intermittently ever since it was first established in 2001. Since May 19, 2015, all of Chinese language Wikipedia has been blocked by the Great Firewall of China [27, 44]. More recently, not just Chinese language Wikipedia, but all language versions of Wikipedia have been blocked from mainland China [2]." (Yang and Roberts 2021])

- **Models Trained Off Wikipedia Vs. Baidu Baike Produce Different Outcomes**
    - "We show that using the pre-trained word embeddings from Baidu Baike and Chinese language Wikipedia with identical training data produces sentiment predictions for news headlines that differ systematically across our categories of interest." (Yang and Roberts 2021])

- **Models Trained Off Chinese Wikipedia Are Significantly More Positive To Ideas Of Democracy Etc. Than Baidu Baike**
    - "The results are largely consistent with what we found in Section 4. Overwhelmingly, Wikipedia predicts headlines that contain target words in the categories of freedom, democracy, election, and collective action to be more positive. In contrast, Baidu Baike predicts headlines that contain target words of figures that the CCP views positively to be more positive. The exceptions to our expectations are the categories of social control, surveillance, CCP, and historical events, where we cannot reject the null of no difference between the two corpuses, although they do not go against our expectations." (Yang and Roberts 2021])
