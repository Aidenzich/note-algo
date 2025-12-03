# 演算法筆記撰寫指南 (Algorithm Note Writing Guidelines)

本文件為此 Repository 中建立新演算法筆記的標準規範（Source of Truth）。所有未來的筆記請根據此指南撰寫。

* **語言**：繁體中文 (Traditional Chinese)。

## 1\. 檔案結構與位置 (File Structure & Location)
  * **目錄命名**：每個題目應有獨立的目錄，通常以題目 ID 命名（例如：`54`, `135`）。
  * **檔案名稱**：筆記檔案一律命名為 `README.md`。  

## 2\. 內容結構 (Content Structure)
`README.md` 必須按順序包含以下章節：

### 2.1 標題 (Header)

  * **格式**：`# [Problem ID]. [Problem Name]`
  * **範例**：`# 135. Candy`

### 2.2 連結 (Link)

  * **內容**：直接連至 LeetCode 題目的連結。
  * **格式**：`https://leetcode.com/problems/...`

### 2.3 分類 (Classify)

  * **標題**：`## Classify`
  * **描述**：簡述輸入格式與高層次的演算法策略（例如：「Two-Pass Algorithm」、「Sliding Window」）。重點在於直觀解釋為何「第一眼」會將此題歸類於此類別。

### 2.4 思路 (Line of thought) — 核心區塊
  * **標題**：`## Line of thought`
  
  * **核心哲學**：**「重過程，輕定義」(Procedural over Declarative)。**
      * 重點在於程式碼*如何*執行，以及變數在物理/邏輯上代表*什麼*，而非僅陳述數學定義。
  * **內容要求**：
    1.  **直觀邏輯 (Intuitive Logic)**：使用具體的比喻來解釋變數的角色（例如：「內層迴圈 `j` 就像切字串的刀子」、「指標 `i` 是有效視窗的邊界」）。除非絕對必要，否則避免抽象的數學公式（如 $DP[i] = \exists j...$）。
    2.  **具體追蹤 (Concrete Trace) [關鍵]**：你**必須**提供一個具體的範例，展示迴圈或遞迴如何展開。
          * **格式**：使用文字區塊 (text block) 顯示每一步驟的 `i`, `j` 與資料狀態。
          * **範例**：
            ```text
            # i: 1, j:0 -> checking s[0:1]
            # i: 2, j:0 -> checking s[0:2] | j:1 -> checking s[1:2]
            ```
    3.  **視覺輔助 (Visual Aids)**：使用 ASCII 藝術、偽代碼 (pseudo-code) 區塊或圖表來解釋指標的移動。

### 2.5 解法 (Solution)

  * **標題**：`## Solution`
  * **不同解法的複雜度**：`### Time O(X), Space O(Y)`
  * **程式碼**：
      * 語言：Python
      * 包在 `python` 程式碼區塊中。
      * 包含完整的 `class Solution` 實作。
      * **註解**：程式碼註解應遵循「直觀邏輯」風格，解釋區塊的*意圖*（例如：「檢查左半部是否有效」），而非單純翻譯語法。

### 2.6 陷阱與筆記 (Traps & Notes)（如適用）
  * **格式**：`⚠️ 常見陷阱 (Trap): [Description]`
  * **內容**：提及邊界情況 (edge cases)、常見錯誤或需留意的邊界條件。

## 3\. 風格指南 (Style Guidelines)
* **語氣**：**直觀與抽象 (Intuitive)**。
    * 寫作對象是正在實作程式碼的開發者，而不是正在證明定理的數學家。
    * 使用物理動詞（如 "slide" 滑動, "expand" 擴張, "cut" 切割, "jump" 跳躍）來描述演算法過程導向。
    * 你的目標是讓讀者能理解你的想法，而不是用數學的「宣告導向」：雖然它在邏輯上是嚴謹的 Proof-correct，但它迫使讀者先去理解這個數學符號，再自己腦補轉換成程式碼的迴圈行為。這是在設「門檻」。對於一個已經知道要寫 Code 的人來說，這個轉換過程是多餘的腦力消耗
* **簡潔性**：偏好清晰、按部就班的邏輯流，勝過晦澀的一行文與冗長的數學式。
* **排版**：善用 Markdown 功能（列表、粗體文字、程式碼區塊）來提升可讀性。避免整面牆的純文字 (walls of text)。
