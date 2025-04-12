# cloud_native_hw2

這個專案練習如何設置 GitHub Actions 來執行 Python 程式碼，根據不同的分支來控制 Action 成功或失敗。

## 功能
使用 GitHub Actions 自動化測試 Python 程式碼。
根據不同分支的程式行為來決定工作流程的成功或失敗。

安裝並測試 requests 套件，向 GitHub API 發送請求並檢查回應。

## 分支說明
- hw1-p :
Python 程式碼會成功執行並且安裝 requests 套件。
程式會向 GitHub API 發送請求並顯示回應狀態碼。
- hw1-f :
程式碼會因為輸入為負數而失敗，並回傳錯誤狀態，導致 GitHub Action 失敗。