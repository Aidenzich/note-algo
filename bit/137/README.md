# 137. Single Number II

https://leetcode.com/problems/single-number-ii/

## Classify

* **Bit Manipulation (位元運算)**
* **Finite State Machine (有限狀態機)**

這題本質上是在設計一個**數位電路**。我們需要一個計數器，針對每個 bit 的出現次數進行計數，並且在數到 3 的時候自動歸零 (Mod 3 Counter)。

## Line of thought

在解題之前，我們先複習（或學習）這題會用到的三個核心工具。請把位元運算想像成對每個 bit 獨立操作的微型機械。

### 1. 核心工具箱 (The Toolset)

1.  **XOR (`^`) - 無進位加法 / 開關 (Toggle)**
    * 邏輯：不一樣為 1，一樣為 0。
    * **直覺**：把它當成一個開關。對同一個變數做兩次 XOR 某個數，會抵銷回到原狀（$A \oplus B \oplus B = A$）。
    * 在本題用途：模擬「加法」。$0 \to 1$。

2.  **AND (`&`) - 過濾器 / 交集 (Filter)**
    * 邏輯：兩個都是 1 才是 1。
    * **直覺**：它是一個守門員。`A & B` 只有在 B 是 1 的時候，A 才能通過；否則被強制變為 0。
    * 在本題用途：檢查狀態轉移條件。

3.  **NOT (`~`) - 反轉 (Invert)**
    * 邏輯：0 變 1，1 變 0。
    * **直覺**：與 AND 配合使用，`A & ~B` 的意思是「**從 A 裡面扣掉 B**」或是「**只有在 B 不存在時，A 才保留**」。這在本題非常關鍵，用來處理「歸零」邏輯。

---

### 2. 邏輯構建 (Core Logic)

每個整數有 32 個 bits。我們要把這 32 個 bits **拆開來看**，每個 bit 位置都是獨立的戰場。
對於任意一個 bit 位置，輸入的數字流會不斷衝擊這個位置（0 或 1）。

**狀態機設計：**
因為除了答案出現 1 次，其他都出現 3 次，所以我們的計數器狀態變化是：
`0次 -> 1次 -> 2次 -> 3次(歸零)`

因為一個 bit 只能存 0 或 1，無法表達三種狀態（0, 1, 2），我們需要**兩個變數**來組合成這個計數器：
* `ones`: 負責記錄「目前累積次數 mod 3 為 **1**」的 bits。
* `twos`: 負責記錄「目前累積次數 mod 3 為 **2**」的 bits。

**狀態流轉圖：**
我們想像一下 `ones` 和 `twos` 是兩個籃子。當一個新的 bit (`num`) 進來時：

1.  **若籃子都空 (State 00)**：`num` 掉進 `ones`。
2.  **若 `ones` 有球 (State 01)**：`num` 進來，`ones` 的球滿了溢出，掉進 `twos`，`ones` 變空。
3.  **若 `twos` 有球 (State 10)**：`num` 進來，觸發「集滿三次」，`twos` 的球清空，`ones` 保持空（全部歸零）。

### 3. 公式推導 (Intuitive Derivation)

不要死背 Truth Table，我們用「句子」寫程式。

**Step 1: 更新 `ones`**
* **目標**：如果 `num` 來了，我們要讓 `ones` 翻轉（加法）。但是！如果 `twos` 裡面已經有東西（代表現在是狀態 2），加 1 會變成狀態 3（歸零），這時候 `ones` 不應該變成 1，而應該維持 0。
* **原始邏輯**：`ones = ones ^ num` (單純加法)
* **加入限制**：只有在 `twos` 是空的 (0) 時候，才允許 `ones` 變為 1。如果 `twos` 是 1，`ones` 必須被強制歸零。
* **程式碼**：`ones = (ones ^ num) & ~twos`
    * `(ones ^ num)`：嘗試把球放進 `ones`。
    * `& ~twos`：守門員說：「只有 `twos` 是 0 的部分，才准通過」。

**Step 2: 更新 `twos`**
* **目標**：`twos` 什麼時候變 1？當 `ones` 已經滿了（狀態 1），又來了一個 `num`，這時候 `ones` 歸零，`twos` 接收進位變 1。或者 `twos` 原本是 1，沒有 `num` 來干擾。
* **簡化邏輯**：其實 `twos` 的邏輯跟 `ones` 完全對稱。`twos` 也是在做加法，只是它是在「`ones` 更新完之後」才更新。
* **程式碼**：`twos = (twos ^ num) & ~ones`
    * 注意：這裡的 `ones` 已經是 Step 1 更新過後的**新值**了。
    * 這行意思是：嘗試把球放進 `twos`，但只有在「新的 `ones` 沒有佔用」的情況下才允許（因為如果 `ones` 變 1 了，代表剛變成狀態 1，`twos` 就不該是 1）。

### 4. 具體追蹤 (Concrete Trace)

Input: `nums = [2, 2, 2, 3]`
為了簡化，我們只看這四個數字的**最低位 (Least Significant Bit)**。
2 -> `...10` (LSB 0)
3 -> `...11` (LSB 1)
假設我們只追蹤**第 1 個 bit** (值為 2 的那個位置)：輸入序列是 1, 1, 1, 1。

```text
Initial: ones=0, twos=0

1. Input bit = 1 (來自第一個 2)
   - ones = (0 ^ 1) & ~0 = 1 & 1 = 1  (狀態變 1)
   - twos = (0 ^ 1) & ~1 = 1 & 0 = 0
   State: ones=1, twos=0 (出現 1 次)

2. Input bit = 1 (來自第二個 2)
   - ones = (1 ^ 1) & ~0 = 0 & 1 = 0  (ones 滿了，歸零)
   - twos = (0 ^ 1) & ~0 = 1 & 1 = 1  (進位到 twos)
   State: ones=0, twos=1 (出現 2 次)

3. Input bit = 1 (來自第三個 2)
   - ones = (0 ^ 1) & ~1 = 1 & 0 = 0  (twos擋住了，ones無法變1，因為即將歸零)
   - twos = (1 ^ 1) & ~0 = 0 & 1 = 0  (twos 加爆了，歸零)
   State: ones=0, twos=0 (出現 3 次 -> 歸零 Reset!)

4. Input bit = 1 (來自數字 3)
   - ones = (0 ^ 1) & ~0 = 1
   - twos = (0 ^ 1) & ~1 = 0
   State: ones=1, twos=0 (出現 1 次)

Result: ones=1. 代表這個 bit 在答案中是 1。
````

## Solution

### Time O(N), Space O(1)

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        
        for num in nums:
            # Step 1: 更新 ones
            # 邏輯：做加法 (XOR)，但如果 twos 已經是 1 (代表現在累積兩次了)，
            # 加上這個 num 會變成 3 次 (歸零)，所以 & ~twos 強制讓 ones 為 0。
            ones = (ones ^ num) & ~twos
            
            # Step 2: 更新 twos
            # 邏輯：同理，做加法，但如果新的 ones 已經佔了位置 (代表回到狀態 1)，
            # twos 就不能為 1 (互斥)。
            twos = (twos ^ num) & ~ones
            
        return ones
```

## Traps & Notes

⚠️ **常見陷阱 (Trap): 順序問題**

  * 在更新 `twos` 時，我們使用的是**已經更新過**的 `ones`。這是可行的，不需要使用暫存變數。因為這兩行公式的設計剛好利用了这种前後依賴關係來簡化邏輯（當 `ones` 變成 1 時，`twos` 自動會被 `& ~ones` 清除，這符合狀態 $1 \to 2$ 或 $0 \to 1$ 的互斥性）。

⚠️ **筆記 (Note): 通用性**

  * 這種 `(a ^ num) & ~b` 的模式是設計 Counter 的一種通用技巧。如果是 "Single Number III" (出現 5 次，找 1 次)，我們可能就需要三個變數來模擬 Mod 5 Counter。

