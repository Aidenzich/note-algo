# 演算法筆記撰寫指南 (Algorithm Note Writing Guidelines)

本文件為此 Repository 中建立新演算法筆記的標準規範（Source of Truth）。所有未來的筆記請根據此指南撰寫。

* **語言**：繁體中文 (Traditional Chinese)。

## 1\. 檔案結構與位置 (File Structure & Location)
  * **目錄命名**：每個題目應有獨立的目錄，通常以題目 ID 命名（例如：`54`, `135`）。
  * **檔案名稱**：筆記檔案一律命名為 `README.md`。  

## 2. 面試模擬框架 (UMPIR Framework)

為了模擬真實面試情境，建議在練習與撰寫筆記時遵循 **UMPIR** 框架。這能幫助你將思維結構化，這正是面試官最看重的能力。

*   **U (Understand) - 理解題目**
    *   確認輸入/輸出格式、限制條件 (Constraints)、邊界狀況 (Edge Cases)。
    *   *筆記對應*：思考過程的起點。
*   **M (Match) - 模式識別**
    *   連結類似題目、識別演算法模式 (Pattern Recognition)。
    *   *筆記對應*：**`3.3 分類 (Classify)`**。
*   **P (Plan) - 規劃解法**
    *   規劃解題路徑、複雜度分析、撰寫 Pseudo-code。
    *   *筆記對應*：**`3.4 思路 (Line of thought)`**。這是筆記的核心。
*   **I (Implement) - 實作**
    *   將邏輯轉換為程式碼。
    *   *筆記對應*：**`3.5 解法 (Solution)`**。
*   **R (Review) - 檢驗**
    *   程式碼檢查 (Dry Run)、測試範例。
    *   *筆記對應*：**`3.4 思路`** 中的「具體追蹤」與 **`3.6 陷阱與筆記`**。

## 3\. 內容結構 (Content Structure)
`README.md` 必須按順序包含以下章節：

### 3.1 標題 (Header)

  * **格式**：`# [Problem ID]. [Problem Name]`
  * **範例**：`# 135. Candy`

### 3.2 連結 (Link)

  * **內容**：直接連至 LeetCode 題目的連結。
  * **格式**：`https://leetcode.com/problems/...`

### 3.3 分類 (Classify)

  * **標題**：`## Classify`
  * **描述**：簡述輸入格式與高層次的演算法策略（例如：「Two-Pass Algorithm」、「Sliding Window」）。重點在於直觀解釋為何「第一眼」會將此題歸類於此類別。

### 3.4 思路 (Line of thought) — 核心區塊
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

### 3.5 解法 (Solution)
  * **標題**：`## Solution`
  * **不同解法的複雜度**：`### Time O(X), Space O(Y)`
  * **程式碼**：
      * 語言：Python      

### 3.6 陷阱與筆記 (Traps & Notes)（如適用）
  * **格式**：`⚠️ 常見陷阱 (Trap): [Description]`
  * **內容**：提及邊界情況 (edge cases)、常見錯誤或需留意的邊界條件。

## 4\. 風格指南 (Style Guidelines)
* **語氣**：**直觀與抽象 (Intuitive)**。
    * 寫作對象是正在實作程式碼的開發者，而不是正在證明定理的數學家。
    * 使用物理動詞（如 "slide" 滑動, "expand" 擴張, "cut" 切割, "jump" 跳躍）來描述演算法過程導向。    
* **簡潔性**：偏好清晰、按部就班的邏輯流，勝過晦澀的一行文與冗長的數學式。
* **排版**：善用 Markdown 功能（列表、粗體文字、程式碼區塊）來提升可讀性。
