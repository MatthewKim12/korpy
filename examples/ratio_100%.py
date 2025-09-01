import korpy
print(korpy.korean_ratio("마인크래프트minecraft", style = korpy.PERCENTAGE)) # 40%
print(korpy.fully_korean("마인크래프트minecraft")) # False

# presets
print(korpy.PERCENTAGE) # %.f%%
print(korpy.PERCENTAGE_UNTIL_1) # %.1%%
print(korpy.PERCENTAGE_UNTIL_2) # %.2%%
