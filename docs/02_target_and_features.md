# 02 · Target and Feature Selection

## Target

**`y`**: did the client subscribe to a term deposit? Encoded yes = 1, no = 0.
It is the outcome the campaigns were run for, and predicting it leads directly to a decision: whom to call.

| Candidate target | Type | Why chosen or not |
| --- | --- | --- |
| **y** | binary, 11.7% yes | **Chosen**: the campaign's goal; the score drives the call list |
| housing | binary, 55.6% yes | Says who has a mortgage, not who will buy; no marketing action follows |
| default | binary, 1.8% yes | Too rare (815 rows), and a credit-risk question this data was not collected for |
| balance | numeric, skew 8.4 | Hard to predict from these columns; no clear decision depends on it |

## Feature decisions

15 of the 16 inputs stay; `duration` is removed.

| Feature | Decision | Reason |
| --- | --- | --- |
| duration | **Drop** | **Data leakage**: only known after the call ends, and a 0-second call is always "no". It inflates scores but makes the model unusable before calling |
| pdays, previous, poutcome | Keep, fix the overlap | `pdays = -1` exactly when `previous = 0` (36,954 rows), and `poutcome` is "unknown" for the same clients → add one flag, `contacted_before` |
| campaign | Keep | Calls so far in this campaign, including the current one: known when calling |
| day, month | Keep, with care | Known when the call is scheduled; `month` mixes calendar effects with campaign intensity |
| contact | Keep | Its "unknown" level is a recording gap from May–June, kept as its own category |
| default | Candidate to drop | Rate spread of 5.4 points resting on 815 clients, and 98.2% one value; test with and without |
| age, job, marital, education, balance, housing, loan | Keep | Client profile, all with a clear link to the target |

## Feature groups

| Group | Features |
| --- | --- |
| Client profile | age, job, marital, education, default, balance, housing, loan |
| Current contact | contact, day, month, campaign |
| Campaign history | pdays, previous, poutcome |
