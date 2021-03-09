---
title: "Data And Its (Dis)contents: A Survey Of Dataset Development And Use In Machine Learning"
author: "Chris Albon"
date: 2021-03-01T11:53:49-07:00
description: "Research notes on Paullada et al. 2020"
type: technical_note
draft: false
---

## Summary

[Paullada et al. 2020](https://arxiv.org/abs/2012.05345) conducts a review of the existing research literature around the ethical and socialogical issues around (typical large) datasets commonly used in machine learning such as ImageNet and others.

## Selective Notes

_This note isn't a comprehensive summary of the entire review, just certain takeaways of particular interest._

- Poor Representation
    - Databases of faces under-represent darker skinned faces ([Buolamwini and Gebru 2018](http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf)).
    - Databases of images under-represent non-Western countries ([DeVries et al. 2019](https://arxiv.org/abs/1906.02659)).
    - Databases of images reflect social stereotypes ([Zhao et al. 2017](https://arxiv.org/abs/1707.09457), [Burns et al. 2018](https://arxiv.org/abs/1803.09797)).
    - Database of toxicity labels words associated with queer identifies as toxic ([Dixon et al. 2018](https://research.google/pubs/pub46743/))

- Poor Data Collection
    - Millions of non-consenual pornographic images in large image datasets ([Prabhu and Birhane 2020](https://arxiv.org/abs/2006.16923))
    - Annotating databases with labels is subjective and not ground truth ([Miceli et al., 2020](https://arxiv.org/abs/2007.14886))
    - [Tsipras et al. 2020](https://arxiv.org/abs/2005.11295) argue ImageNet:
        - Applies only one label to an image that might contain multiple objects
        - Crowdworkers (Mechanical Turk, etc.) are biased towards the labeling processes.

- Poor Data Documentation
    - Widespread variation in datasets reporting how they produced their data ([Geiger et al. 2019](https://arxiv.org/abs/1912.08320))

- Miopic Focus On Benchmarks
    - Leaderboards aren't everything ([Ethayarajh and Jurafsky 2009](https://arxiv.org/abs/2009.13888))
    - Performance metrics aren't everything([Bender and Koller 2020](https://www.aclweb.org/anthology/2020.acl-main.463/))

- Data management
    - "... the machine learning community still has much to learn from other disciplines with respect to how they handle the data of human subjects. Unlike in the social sciences or medicine, the machine learning field has yet to develop the data management practices required to store and transmit sensitive human data" (Paullada et al. 2020).
    - Data science should be human subject research and require IRB approval ([Metcalf and Crawford 2016](https://journals.sagepub.com/doi/full/10.1177/2053951716650211)).
    - "However, machine learning researchers developing such datasets rarely pay attention to this necessary consideration. Researchers will regularly distribute biometric information— for example, face image data— without so much as a distribution request form, or required privacy policy in place" (Paullada et al. 2020).

- Data Use And Reuse
    - It might not always be a good idea to take data gathered for one purpose and use it for another purpose.
    - The DukeMTMC database was from eight security cameras around the campus, distributed without the conscent of the individuals in the videos. Eventually the database was taken down but is still widely avaliable online.

- Legal
    - ImageNet uses a number of sources of data where the licensing/copyright are unclear. ImageNet gets around this by not hosting the images themselves.
    - Creative Commons license allows for training of machine learning models from it under fair use doctrine ([Merkely 2019](https://creativecommons.org/2019/03/13/statement-on-shared-images-in-facial-recognition-ai/)])
    - Legal scholars argue it is okay to use copyrighted text to train machine learning models ([Sag 2019](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3331606)).
    - Using copyrighted text can combat bias by creating a larger corpus from which to train on ([Levendowski 2017](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3024938))

- Solution
    - "In closing, we advocate for a turn in the culture towards carefully collected datasets, rooted in their original contexts, distributed only in ways that respect the intellectual property and privacy rights of data creators and data subjects, and constructed in conversation with the relevant scientific and scholarly fields required to create datasets that faithfully model tasks and tasks which target relevant and realistic capabilities. Such datasets will undoubtedly be more expensive to create, in time, money and effort, and therefore smaller than today’s most celebrated benchmarks. This, in turn, will encourage work on approaches to machine learning (and to artificial intelligence beyond machine learning) that go beyond the current paradigm of techniques idolizing scale. Should this come to pass, we predict that machine learning as a field will be better positioned to understand how its technology impacts people and to design solutions that work with fidelity and equity in their deployment contexts." (Paullada et al. 2020).