---
title: "Fundamentals Of Software Architecture"
author: "Chris Albon"
date: 2021-02-11T00:00:00-00:00
description: "Notes on the Fundamentals of Software Architecture."
type: technical_note
draft: false
aliases: [/machine_learning_engineering/fundamentals_of_software_architecture/]
---

_These are notes on Neal Ford and Mark Richards' [Fundamentals of Software Architecture](https://www.amazon.com/Fundamentals-Software-Architecture-Comprehensive-Characteristics/dp/1492043451)._

- Chapter 1: Introduction
    - Eight core expectations of a software architect:
        - Make architecture decisions
            - "An architect is expected to define the architecture decisions and design principles used to guide technology decisions within the team, the department, or across the enterprise."
        - Continually analyze the architecture
            - "An architect is expected to continually analyze the architecture and current technology environment and then recommend solutions for improvement."
        - Keep current with latest trends
            - "An architect is expected to keep current with the latest technology and industry trends."
        - Ensure compliance with decisions
            - "An architect is expected to ensure compliance with architecture decisions and design principles."
        - Diverse exposure and experience
            - "An architect is expected to have exposure to multiple and diverse technologies, frameworks, platforms, and environments."
                - This doesn't mean expertise, rather breadth is valued over depth.
        - Have business domain knowledge
            - "An architect is expected to have a certain level of business domain expertise."
        - Possess interpersonal skills
            - "An architect is expected to possess exceptional interpersonal skills, including teamwork, facilitation, and leadership."
        - Understand and navigate politics
            - "An architect is expected to understand the political climate of the enterprise and be able to navigate the politics."
    - Software development _process_ vs. software engineering _practices_:
        - Process: "By process, we mean how teams are formed and managed, how meetings are conducted, and workflow organization; it refers to the mechanics of how people organize and interact."
        - Practice: "Software engineering practices, on the other hand, refer to process-agnostic practices that have illustrated, repeatable benefit."
    - Laws of Software Architecture
        - First Law: "Everything in software architecture is a trade-off."
        - Second Law: "Why is more important than how."
- Chapter 2: Architectural Thinking
    - Four aspects of thinking like a software architect:
        - One: Understanding the difference beetween architecture and design.
        - Two: Understanding a wide breadth of technical knowledge while maintaining some technical depth.
            - Transitioning from developer means a shift of a focus on depth to a focus breadth, this comes with two common pitfalls:
                - First, Architect tries be an expert in everything, which is impossible.
                - Second, Architect has stale expertise.
                    - The Frozen Caveman Anti-Pattern:
                        - "...the Frozen Caveman Anti-Pattern, describes an architect who always reverts back to their pet irrational concern for every architecture"
        - Three: Understanding trade-offs between solutions and technologies.
            - "Architecture is the stuff you can’t Google."
                - Meaning: The architectural decisions an Architect makes are not the type of thing that comes up in Google searches.
            - "There are no right or wrong answers in architecture—only trade-offs."
        - Four: Understanding the importance of business concerns.
            - "Thinking like an architect is understanding the business drivers that are required for the success of the system and translating those requirements into architecture characteristics"
    - How to balance architectural experience and hands-on coding experience as an architect:
        - While architects should code, they should not be the owner of any critical path for a project. When this happens they become a bottleneck.
        - Instead they should try one of these four things:
            - 1. Code proof of concepts
            - 2. Burn down technical debt
            - 3. Building tools to help te developers work faster.
            - 4. Code reviews.
- Chapter 3: Modularity
    - Much of software architecture is about managing modularity.
    - How to describe and measure modularity:
        - Cohesion: How related of the different parts of the module to each other?
        - Coupling: 
            - Afferent coupling measures the number of incoming connections to a code module
            - Efferent coupling measure the number of outgoing connections from a code module
        - Abstractness:
            - Number of abstract things (abstract classes, etc.) to concerete things (implementations)
        - 
        