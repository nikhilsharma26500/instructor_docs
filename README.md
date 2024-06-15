# Instruct Cookbook

## Table of Contents
- [Zero Shot Prompting](#zero-shot-prompting)
- [Few Shot Prompting](#few-shot-prompting)
- [Ensembling](#ensembling)
- [Self Critcism](#self-critcism)
- [Decomposition](#decomposition)

## [Zero Shot Prompting](https://github.com/nikhilsharma26500/instructor_docs/tree/main/zero_shot)

### Emotion Prompting
It incorporates phrases of psychological relevance to humans (e.g., "This is important to my career") into the prompt, which may lead to improved LLM performance on benchmarks and open-ended text generation.

### Role Prompting
It also known as persona prompting, assigns a specific role to the GenAI in the prompt. For example, the user might prompt it to act like "Madonna" or a "travel writer". This can create more desirable outputs for open-ended tasks and in some cases improve accuracy on benchmarks.

### Style Prompting
It involves specifying the desired style, tone, or genre in the prompt to shape the output of a GenAI. A similar effect can be achieved using role prompting.

### System 2 Attention (S2A)
first asks an LLM to rewrite
the prompt and remove any information unrelated to the question therein. Then, it passes this new prompt into an LLM to retrieve a final response.

### SimToM
### RaR
### RE2
### Self-Ask

## Few Shot Prompting

### Example Generation
### Example Ordering
### Exemplar Selection

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