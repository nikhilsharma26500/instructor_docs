# Instruct Cookbook

All definitions and ideas are taken from [The Prompt Report: A Systematic Survey of Prompting Techniques](https://arxiv.org/abs/2406.06608)

## Table of Contents
- [Zero Shot Prompting](#zero-shot-prompting)
- [Few Shot Prompting](#few-shot-prompting)
- [Ensembling](#ensembling)
- [Self Critcism](#self-critcism)
- [Decomposition](#decomposition)

## [Zero Shot Prompting](https://github.com/nikhilsharma26500/instructor_docs/tree/main/zero_shot)

### [Emotion Prompting](https://github.com/nikhilsharma26500/instructor_docs/blob/main/zero_shot/emotional_prompting.py) 
It incorporates phrases of psychological relevance to humans (e.g., "This is important to my career") into the prompt, which may lead to improved LLM performance on benchmarks and open-ended text generation.

### [Role Prompting](https://github.com/nikhilsharma26500/instructor_docs/blob/main/zero_shot/role_prompting.py)
It also known as persona prompting, assigns a specific role to the GenAI in the prompt. For example, the user might prompt it to act like "Madonna" or a "travel writer". This can create more desirable outputs for open-ended tasks and in some cases improve accuracy on benchmarks.

### [Style Prompting](https://github.com/nikhilsharma26500/instructor_docs/blob/main/zero_shot/style_prompting.py)
It involves specifying the desired style, tone, or genre in the prompt to shape the output of a GenAI. A similar effect can be achieved using role prompting.

### [System 2 Attention (S2A)](https://github.com/nikhilsharma26500/instructor_docs/blob/main/zero_shot/system_2_attention.py)
It first asks an LLM to rewrite the prompt and remove any information unrelated to the question therein. Then, it passes this new prompt into an LLM to retrieve a final response.

### [SimToM](https://github.com/nikhilsharma26500/instructor_docs/blob/main/zero_shot/sim_to_m.py)
It deals with complicated questions which involve multiple people or objects. Given the question, it attempts to establish the set of facts one person knows, then answer the question based only on those facts. This is a two prompt process and can help eliminate the effect of irrelevant information in the prompt.

### [Rephrase and Respond (RaR)](https://github.com/nikhilsharma26500/instructor_docs/blob/main/zero_shot/rephrase_and_respond.py)
It instructs the LLM to rephrase and expand the question before generating the final answer. For example,
it might add the following phrase to the question: "Rephrase and expand the question, and respond". This could all be done in a single pass or the new question could be passed to the LLM separately. RaR has demonstrated improvements on multiple benchmarks.

### [Re-reading (RE2)](https://github.com/nikhilsharma26500/instructor_docs/blob/main/zero_shot/re_reading.py)
It adds the phrase "Read the question again:" to the prompt in addition to repeating the question. Although this is such a simple technique, it has shown improvement in reasoning benchmarks, especially with complex questions.

### [Self-Ask](https://github.com/nikhilsharma26500/instructor_docs/blob/main/zero_shot/self_ask.py)
It prompts LLMs to first decide if they need to ask follow up questions for a given prompt. If so, the LLM generates these questions, then answers them and finally answers the original question.

## Few Shot Prompting

### Exemplar Generation
#### [Self-Generated In-Context Learning (SG-ICL)](https://github.com/nikhilsharma26500/instructor_docs/blob/main/few_shot/example_generation/sg_icl.py)
It leverages a GenAI to automatically generate exemplars. While better than zeroshot scenarios when training data is unavailable, the generated samples are not as effective as actual data.

### Exemplar Ordering

### Exemplar Selection
#### [K Nearest Neighbors (KNN)]()
is part of a family of algorithms that selects exemplars similar to $D_{x_i}^{\text{test}}$ to boost performance. Although effective, employing KNN during prompt generation may be time and resource intensive.

#### [Vote-K]()
It is another method to select similar exemplars to the test sample. In one stage, a model proposes useful unlabeled candidate exemplars for an annotator to label. In the second stage, the labeled pool is used for Few-Shot Prompting. Vote-K also ensures that newly added exemplars are sufficiently different than existing ones to increase diversity and representativeness.

## Thought Generation

### Chain-of-Thought (CoT)

## Ensembling

### COSP
### DENSE
### DiVeRSe
### Max Mutual Information
### MoRE
### Self-Consistency
### Universal Self-Consistency
### USP
### Prompt Paraphrasing

## Self Critcism

### Chain-of-Verification
### Self-Calibration
### Self-Refine
### Self-Verification
### ReverseCoT
### Cumulative Reason

## Decomposition

### DECOMP
### FAITHFUL CoT
### Least-to-Most
### Plan-and-Solve
### Program-of-Thought
### Recurs.-of-Thought
### Skeleton-of-Thought
### Tree-of-Thought