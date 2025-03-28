
# Homework 2: Data Cleaning

**Name:** Ray Saleh
**Class:** CS625-HW2  
**Due Date:** February 09, 2025  

## Part 1. Data Cleaning

### 1. Remove Rows/Columns

**i. How were blank rows, misleading values, and unnecessary columns removed?**  
1. Removed Gross Column as per requested in the instructions.
2. Text Facet checked columns to verify that there were no misleading information. 
3. Checked if any rows were completly blank and removed them.

**ii. Criteria for Removing Rows Containing Misleading Information:**  
1. If rows were completly empty, remove said rows.
2. If information did not match requirements in row, remove said row.

---  

### 2. Refilling Values in Columns

1. **Numerical Columns (`RATING`, `VOTES`, `RunTime`):**  
   - Fill blank cells with 0s using GREL for the columns ('Rating', 'Votes', 'RunTime')
   ```
   if(isBlank(value),0,value)
   ```

2. **Text Columns to Numerical Columns:**  
   - Convert Columns to numbers: Facet -> Edit Cells -> Common Transformations -> to numbers

---  

### 3. Cleaning the "Year" Column

**i. Removing Ambiguous Values:**  
- Removed rows with Roman numerals or non-year strings in the "Year" column.  

**ii. Replacing Year Formats:**  
- Manually Selected each year using facet that contains one year (Start date only), or has words or roman numerals because it was easier than removing only sybols and letters
    ```
    value.replace(/((\d{4})\D?.*)/, "$1")
    ```  
- Remove all instances of roman numerals
    ```
    value.replace(/\(\s*[IVXLCDM]+\s*\)/, "")
    ```
- remove everything but numbers for a final time
    ```
    (value.replace(/[^0-9–-]/, "").trim())
    ```

**iii. Creating `startYear` and `endYear`:**  
- Extracted start and end years using GREL:  
  - For `startYear`:  
    ```
    value.split(/[-–]/)[0]
    ```  
  - For `endYear`:  
    ```
    if(value.contains(/[-–]/), value.split(/[-–]/)[1], value.split(/[-–]/)[0])
    ```  

- Removed the original "Year" column after extracting the necessary data.  

---  

### 4. Creating the "Verdict" Column

- Added a new column **"Verdict"** based on the `RATING` column using GREL:  

    ```
    if(value == 0, "Not Known",
        if(and(value > 0, value <= 4.5), "Flop",
            if(and(value > 4.5, value <= 6.5), "Average",
                if(and(value > 6.5, value <= 8.0), "Hit",
                    if(value > 8.0, "Super Hit", value
                    )
                )
            )
        )
    )
    ```  

---  

## Part 2. Analyze Cleaned Data

1. **How many movies were listed as “Super Hit” in the year 2021?**  
   - In my work there were 26 Super Hits in the year 2021.

2. **Which movie got the highest rating in the years 2018 to 2020 by genre (one movie for each genre)?**  
   - Action: Chen qing ling, 2019
   - Adventure: Sa-rang-eui bul-sa-chak, 2019
   - Animation: Demon Slayer: Kimetsu No Yaiba, 2019
   - Biography: When They See Us, 2019
   - Comedy: Kota Factory, 2019
   - Crime: The Flower of Evil, 2020
   - Documentary: Our Planet, 2019
   - Drama: Naui Ajusshi, 2018
   - Family: Emily's Wonder Lab, 2020
   - Fantasy: The King: Youngwonui Gunjoo, 2020
   - Game-Show: The Circle, 2020
   - History: The Coldest Game, 2019
   - Horror: Anjaan: Special Crimes Unit, 2018
   - Music: Ben Platt Live from Radio City Music Hall, 2020
   - Musical: Westside, 2018
   - Mystery: Run, 2020
   - News: The Weekly with Wendy Mesley, 2018
   - Reality-TV: Car Masters: Rust to Riches, 2018
   - Romance: Gaya sa pelikula, 2020
   - Sci-Fi: Stories from Our Future, 2019
   - Short: 8:46, 2020
   - Sport: Wang Qiu Shao Nian, 2019
   - Talk-Show: Stranger Things: Spotlight, 2018
   - Thriller: Black Earth Rising, 2018
   - War: 21 Sarfarosh Saragarhi 1897, 2018

3. **List the top 3 genres (no duplicates) that got the lowest number of votes (excluding 0):**  
   - War: 364 votes
   - News: 1879 votes
   - Sport: 3936 votes

4. **Name the director who directed the 10-minute run time movie in the year 2020 that received the highest number of votes. Include the movie name, number of votes, and genre:**
   - **Director:** Hong Won-ki
   - **Movie:** Goedam
   - **Votes:** 694
   - **Genre:** Short

5. **List the top 5 movies that received the highest number of votes but have the verdict "Flop":**  
   - **Death Note** (2017) - **Votes:** 79,452
   - **The Human Centipede (First Sequence)** (2009) - **Votes:** 75,214
   - **Scary Movie 5** (2013) - **Votes:** 67,762
   - **365 dni** (2020) - **Votes:** 63,620
   - **Sharknado** (2013) - **Votes:** 47,705


---  

## References  
- [OpenRefine GREL Functions](https://openrefine.org/docs/manual/grelfunctions)  
- Dataset: [Kaggle Movies Dataset](https://www.kaggle.com/datasets/bharatnatrayn/movies-dataset-for-feature-extracion-prediction?resource=download)  
