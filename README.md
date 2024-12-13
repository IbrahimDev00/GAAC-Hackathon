# Real-Time Event Tracking with Probabilistic Data Structures

## Problem Statement

In this project, the goal is to design a **probabilistic data structure** that tracks the frequency of millions of **real-time events** while maintaining **minimal memory usage** and supporting **accurate percentile queries**.

### Key Requirements:
- **Sub-linear space complexity** while maintaining accuracy.
- **Mergeable properties** for distributed environments.
- Efficiently track event frequency and provide quantile estimates (percentiles).
- Minimize collisions in the hashing process.

## Solution Approach

To tackle this problem, we utilize a combination of three key probabilistic data structures:

1. **CLHash** - A hash function used to process events efficiently.
2. **Cuckoo Filter** - For membership testing to check if an event has been seen before.
3. **Count-Min Sketch** - To track the frequency of events in a memory-efficient way.
4. **KLL Sketch** - To calculate quantile distributions (e.g., top-k frequencies, percentiles) from the frequency data.

### Workflow:
1. **Hashing with CLHash**:  
   - Each incoming event is hashed using the **CLHash** algorithm, which is optimized for frequency counting and minimizes memory usage.
   
2. **Cuckoo Filter**:  
   - The hashed value is then passed to a **Cuckoo Filter** to check whether the event has been seen before:
     - If **known**, the event's frequency is updated in the **Count-Min Sketch**.
     - If **unknown**, the event is added to the **Cuckoo Filter** and subsequently passed to the **Count-Min Sketch**.
   
3. **Count-Min Sketch**:  
   - This data structure tracks the frequency of each event in a compressed manner. The event's hash is used to update the frequency counts, allowing for **sub-linear space complexity** while still providing accurate frequency estimates.
   
4. **KLL Sketch**:  
   - Finally, the frequency data from the **Count-Min Sketch** is processed by the **KLL Sketch** to estimate quantile distributions (e.g., top-k events, percentiles). This allows for **efficient quantile estimation** without needing to maintain all the frequency data.

5. **Output**:  
   - The final output consists of **quantile estimates**, providing insights into the distribution of event frequencies.

![Blank diagram (3)](https://github.com/user-attachments/assets/39adf796-48c6-4c53-81e4-143b9947c34c)

## Technology Stack

- **Programming Language**:  
  - **Python** (for rapid prototyping and ease of implementation).
  
- **Hashing Algorithm**:  
  - **CLHash** (optimized for frequency counting with minimal memory overhead).

- **Data Structures**:
  - **Cuckoo Filter** (for membership testing).
  - **Count-Min Sketch** (for efficient frequency tracking).
  - **KLL Sketch** (for quantile estimation).

- **Libraries/Tools**:
  - **Pyhash** (for hashing implementation).
  - **cuckoo-filter v-1.0.6** (for the cuckoo implementation).


## Challenges and Potential Issues

### 1. **Memory Overhead**:
   - Despite using probabilistic data structures, memory usage can still become a challenge when handling millions of events. This can be mitigated by carefully tuning the **hash function parameters** and the **size of the data structures**.

### 2. **Collision Handling**:
   - Hash collisions could lead to inaccurate frequency estimates or membership tests. Using a **Cuckoo Filter** helps minimize this risk, but tuning its parameters (like the number of hash functions) is crucial to avoid excessive false positives or false negatives.

### 3. **Real-Time Performance**:
   - Real-time event processing requires the system to be fast and efficient. The **CLHash** function and the use of efficient data structures (like **Count-Min Sketch** and **KLL Sketch**) are crucial to ensure the system can handle large volumes of events without significant lag.

### 4. **Handling Distributed Environments**:
   - In distributed environments, merging data across multiple nodes could introduce additional challenges in maintaining consistency. The **Cuckoo Filter** and **Count-Min Sketch** have mergeable properties, but merging the data correctly while ensuring accuracy can be complex.

## Implementation Details

### 1. **Hashing with CLHash**:
   - **CLHash** is applied to each event to produce a hash value. This hash value is used to insert the event into the **Cuckoo Filter** and **Count-Min Sketch**.

### 2. **Cuckoo Filter**:
   - The **Cuckoo Filter** checks whether an event has already been seen. If it has, it passes to the **Count-Min Sketch** for frequency updates. If not, it is added to the filter.

### 3. **Count-Min Sketch**:
   - The **Count-Min Sketch** algorithm updates the frequency of the event. It is designed to give **approximate frequency counts** using minimal memory.

### 4. **KLL Sketch**:
   - The **KLL Sketch** is used to calculate quantile distributions. It processes the output of the **Count-Min Sketch** to estimate the quantiles and provide useful statistics (e.g., percentiles, top-k items).

## Reason for Choosing Technologies
- **CLHash**: Provides memory-efficient hashing with a focus on frequency estimation. Ideal for scenarios where large datasets need to be processed quickly with minimal memory usage.

- **Cuckoo Filter**: Offers low collision rates and efficient membership testing, making it a perfect fit for the task of checking if an event has already been encountered.

- **Count-Min Sketch**: This structure is known for sub-linear space complexity and efficient frequency tracking, which is essential when processing millions of real-time events.

- **KLL Sketch**: Provides an approximate quantile estimation without requiring the full dataset, making it well-suited for analyzing top-k or percentile data in large-scale systems.



