import os
import facebook
import time
baseName='數字營銷'
UniqueDatabaseID_1='122096036522017006'
hackingDatabase_1='EAAOrLOAqRl4BOZC69Lq3cF1zZAXVvID31BEEZB0aCBp39PFBuiPOZCqjnJI4SEZApiRn6NpQequF8r9iByCZBUKQ67LzAH95DVdup7yCKXWFNT7C4iha3RNDWxJgMYj9dZCYkVYQRfN0AFI9zZBaOto6ZBFYcZCjMFoxZAilT67j44ffzL4txwaInWZBsZAnNfDq12pNqiQZDZD'
baseName='搜索引擎优化精英团队'
UniqueDatabaseID_2='104056472793404'
hackingDatabase_2='EAAOrLOAqRl4BO5a5qFW9TfyGH5obqpooC6GUNa6dVZBu61ImxQeW3j7uDaAZBfqyjaAJHA2o7V4pWGELJO72FBGgDBTXCZBE7y7Mbtn0KaLL69AhiCPf4n8HMezbikPi2vZC1ohlaFV16N0XRDIg4Lo69Ar1ZAkt1MY3uAhwkiEqvgFcUZBZB3ZCai7AtMBsH48ZD'
baseName='商業服務'
UniqueDatabaseID_3='107388409123273'
hackingDatabase_3='EAAOrLOAqRl4BOZCZA4K9lwZBfHpr1KRudRPaQ7vN4fXxOkGyqzWnGHkGpqNBhwWR1YjKsIL08DlspLny3LozJtMUPpWsdGNEVMfPMZASRz5nP3IU5Q4lVZCtO3ixgQkELHOLQNEXoYCh7SG6UZAOBbl4CxMtWAQIACX6mcqL4P070L5z4N1SXHeBeM7hcKSZCIZD'
baseName='電子郵件數字營銷'
UniqueDatabaseID_4='102800762919590'
hackingDatabase_4='EAAOrLOAqRl4BOxiu8DZCCzaMwYrj3lvS3i853v6AtWbZAmretwoi9KbyNmrryRwyLBQQmEy2QaEAgcpZBXVEc6QkFePzeE8UQ0JTyAvah8aD9BlA49Tqc1FmBYU8nTgGltIvzPOeq8j1Lj6raCMBnUFkUmifPVYlsRP1PHQA30DneQLEFnaOzeXztxgTHsZD'
baseName='電報營銷'
UniqueDatabaseID_5='116207588232052'
hackingDatabase_5='EAAOrLOAqRl4BO2u2lwKNvOBZBHuKvhMSGOKC3pXRpls1KHIFz3b9ZC4NCqymzZAyOw8gFr3eqDmXetPtaNiZBbaoTrZAGcrykKI6RKZAHpsc55ZAaQaiAi6eXAueirmnaTmZA82oaMZA08RPSAmgYNXzRvMovacEc5Vt1lcJnZBz989xlN3O0DpUlsgIKzCtQJbToZD'
baseName='数字营销利器'
UniqueDatabaseID_6='101282356406731'
hackingDatabase_6='EAAOrLOAqRl4BOwdDv9wJ1djLeMEWvhC2dB8bcWVhbZAMKLGEMfVyFcwg0IQmgVtfIgNN5CADG9Ar9iSvqHJGnED9NWDe5N0TjhZBKdiid3kDAY3k5ZBYQqZABiJPHvK8WR93w1I7THJJ6hZCamZBVHJUhAcBp47j8Mh1VrqfKe1ylbjFWFk31WsEYrZCZAkzDgkZD'
baseName='數字營銷搜索引擎優化'
UniqueDatabaseID_7='101771403023782'
hackingDatabase_7='EAAOrLOAqRl4BOzOMjgaKyCNkb1hn3aZAajTpN240NZAsK4ayRyEGK6dTH8bqeE7ojjAq8Kskm9wQ5LPA2ptZB60GAzToT9uZCy7DOj5jy8rJIvMhoXNEwB7cRtEYE2TyNxQHPOkBHp0ePVXVmJm2qwgeUWvKZA6gtiElLbKBumWnST17Y40rZA4M1S5vB4rLMZD'
baseName='電話號碼數字營銷'
UniqueDatabaseID_8='104499862747819'
hackingDatabase_8='EAAOrLOAqRl4BOZBS86AZBYlDFyPcdMwbnvYUZAbTOVN0Bk5BZCnp3ZBmn9Q3mZCA1H31625yfsPf5cQZAy2ajsQvSKMaAaKlyTMz38JHTByyhzibgY3nv7YAqAkjcUMcBpr2VogqY84f5OySlgvrVQ8vYsmy9I8wLxWHg2HgLWUbB5ZA5NjXEtwTZAkf2gSvfAowZD'
baseName='數字營銷'
UniqueDatabaseID_9='112639981925038'
hackingDatabase_9='EAAOrLOAqRl4BO4eMxIiSbDvXaDC23nmmJFKlqIscjR3J7kJYebZADtyYhqWNfeXDvO7rXixZCySZAfMR4bUyUXdiUKZBlb6CA1EC15wxwOpnbhLggt0kjuJDIENf4r4aKaHdtr9iR5EpR6l3ZAoPZCd30RZCXk7DCVciZA8urM5HDk1mnUMCGWR4D0MstjQXd9gZD'
baseName='企業營銷服務'
UniqueDatabaseID_10='114179371768712'
hackingDatabase_10='EAAOrLOAqRl4BO5MkPXlH72i2K2zZCYm91iauY1VsKAkQEhjbICSlzJ75z0elaq7nZAH6LXtmQazUN21H6A0EkzkRQ3nG4bqqypWQPBlxNAbjA7YBFCyK8xi3RdCbaW6Wo4H9RdBy8tbDu8HwRIzVoud4W5NO0wvJomjZByo1MNyIbCZAUpQfmQa4aNbkKE8ZD'
baseName='数字营销解决方案'
UniqueDatabaseID_11='104049806125782'
hackingDatabase_11='EAAOrLOAqRl4BO1CgPeZASlZCo5tFS7C7eVZCjunURuJRUmDMlMFNAT5zl32Rv3hW2UUtGZB0uFyafipFO79Bv6IY580Lr2RIAzhFv4tt1qwUiszyOIb4ZCptt97vO254OIllBHhELfocq3yDpEYwx2ivsH94hdmAw6UA6fmDRJxxgC8HvHQpMdW8ZAjsdR5SgZD'
baseName='数码营销服务'
UniqueDatabaseID_12='111790878668954'
hackingDatabase_12='EAAOrLOAqRl4BO7L17yMcVpQsMXi6WdEVsb3gb4p01QYODC29VxB65XpFjZC0MGUnO2usioHDMYiwNXmVom1JS4ZCAr99APyYtCZCetKtCf9rkX2vZCu6aoVB6MT2CgoS7JIbJKbIvJs8dy2UD5x5bysiMnS7PS8mDnJBF8425MWJ2E7klgpuvMw2l4tzuvIZD'
# Define an array of access tokens and page IDs
access_tokens = [ hackingDatabase_1, hackingDatabase_2, hackingDatabase_3, hackingDatabase_4, hackingDatabase_5, hackingDatabase_6, hackingDatabase_7, hackingDatabase_8, hackingDatabase_9, hackingDatabase_10, hackingDatabase_11, hackingDatabase_12 ]
page_ids = [ UniqueDatabaseID_1, UniqueDatabaseID_2, UniqueDatabaseID_3, UniqueDatabaseID_4, UniqueDatabaseID_5, UniqueDatabaseID_6, UniqueDatabaseID_7, UniqueDatabaseID_8, UniqueDatabaseID_9, UniqueDatabaseID_10, UniqueDatabaseID_11, UniqueDatabaseID_12 ]
# some secret
art_process_end_fire="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠒⠋⠉⠉⠉⠉⠉⠙⠒⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠁⠀⠀⠀⣀⣀⣠⠤⠤⠤⠤⠤⣄⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡥⠴⠒⠊⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⡀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣷⣤⣀⠈⡆⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⣸⣿⣿⣶⣤⡀⠀⣴⣿⡟⢉⠀⠀⠀⠉⠀⢸⡀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⢀⣩⡛⢿⠉⡍⠛⣷⣾⣿⣷⢤⠴⠷⢄⣇⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡧⢰⣿⣿⣿⠇⠀⣷⠀⠉⠉⠉⠉⠀⠀⠀⠸⢿⠥⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⢀⠀⢹⣦⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⢀⡀⢠⡀⢛⣁⣬⠆⠉⠉⣱⡿⡍⠀⢸⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⢺⣧⣀⣈⣿⣿⣿⣷⣤⣴⣶⡿⣻⠁⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡎⢿⠛⠛⠛⣿⣾⣏⣩⠍⠀⡸⠃⠀⣰⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢮⡳⡌⠉⠻⣿⡿⠀⠀⠼⠁⢠⠞⡟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⢄⠀⠀⣿⣿⠀⠀⢀⡜⠁⠚⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡞⠈⠻⣗⠦⠽⠿⠤⠞⠁⠀⠀⠀⠀⣿⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠞⠁⣇⠀⠀⠈⠳⢄⡀⠀⠀⠀⠀⠀⠀⢀⡟⢸⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣀⡠⠤⠖⠒⠋⠉⡇⠀⠀⢹⡀⠀⠀⠀⠀⠙⠲⢤⡀⠀⢀⡴⠋⠀⢀⡇⠉⠲⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⠤⠒⠋⠉⠀⠀⠀⠀⠀⠀⢰⣧⠀⠀⠈⣧⠀⠀⠀⠀⠀⠀⠀⡹⠓⠋⠲⡄⠀⠈⣧⠀⠀⠸⡍⠙⠲⠤⣄⣀⠀⠀⠀⠀⠀
⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡿⠀⠀⠀⢻⡳⣄⠀⠀⠀⣠⠞⠀⠀⠀⠀⠘⣆⠀⣾⡄⠀⠀⠹⡄⠀⠀⠀⠈⠉⠒⢤⡀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡇⠀⠀⠀⠈⣇⠈⢣⡀⣰⢳⡀⠀⠀⠀⢀⡞⠉⠶⠁⢧⠀⠀⠀⢱⡀⠀⠀⠀⠀⠀⠀⢧⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⢸⡀⠀⠙⠇⠀⢹⠒⠒⠒⢯⠀⠀⠀⠀⢸⡀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠘⣆
⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠂⠀⠀⠸⠇⠀⠀⠀⠀⠟⠀⠀⠀⠈⠧⠀⠀⠀⠘⠇⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠻
⠀⠀⠀⠁⠁⠀⠁⠀⠀⠀⠀⠈⠀⠀⠀⠈⠉⠉⠋⠉⠉⠉⠉⠁⠉⠉⠀⠉⠈⠁⠉⠉⠛⠛⠋⠉⠉⠉⠉⠉⠉⠉⠉⠀⠈⠀⠀
  _______ _            ______           _ 
 |__   __| |          |  ____|         | |
    | |  | |__   ___  | |__   _ __   __| |
    | |  | '_ \ / _ \ |  __| | '_ \ / _` |
    | |  | | | |  __/ | |____| | | | (_| |
    |_|  |_| |_|\___| |______|_| |_|\__,_|


"""
art_hacker_2 =""" 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠃⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠾⢛⠒⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⣄⡈⠓⢄⠠⡀⠀⠀⠀⣄⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⠀⠈⠱⡄⠑⣌⠆⠀⠀⡜⢻⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠳⡆⠐⢿⣆⠈⢿⠀⠀⡇⠘⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⡇⠀⠀⠈⢆⠈⠆⢸⠀⠀⢣⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⠀⠀⠈⢂⠀⡇⠀⠀⢨⠓⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣦⣤⠖⡏⡸⠀⣀⡴⠋⠀⠈⠢⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠁⣹⣿⣿⣿⣷⣾⠽⠖⠊⢹⣀⠄⠀⠀⠀⠈⢣⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⣇⣰⢫⢻⢉⠉⠀⣿⡆⠀⠀⡸⡏⠀⠀⠀⠀⠀⠀⢇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡇⡇⠈⢸⢸⢸⠀⠀⡇⡇⠀⠀⠁⠻⡄⡠⠂⠀⠀⠀⠘
⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠛⠓⡇⠀⠸⡆⢸⠀⢠⣿⠀⠀⠀⠀⣰⣿⣵⡆⠀⠀⠀⠀
⠈⢻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣦⣀⡇⠀⢧⡇⠀⠀⢺⡟⠀⠀⠀⢰⠉⣰⠟⠊⣠⠂⠀⡸
⠀⠀⢻⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢧⡙⠺⠿⡇⠀⠘⠇⠀⠀⢸⣧⠀⠀⢠⠃⣾⣌⠉⠩⠭⠍⣉⡇
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣋⠀⠈⠀⡳⣧⠀⠀⠀⠀⠀⢸⡏⠀⠀⡞⢰⠉⠉⠉⠉⠉⠓⢻⠃
⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣀⠠⠤⣤⣤⠤⠞⠓⢠⠈⡆⠀⢣⣸⣾⠆⠀⠀⠀⠀⠀⢀⣀⡼⠁⡿⠈⣉⣉⣒⡒⠢⡼⠀
⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣎⣽⣶⣤⡶⢋⣤⠃⣠⡦⢀⡼⢦⣾⡤⠚⣟⣁⣀⣀⣀⣀⠀⣀⣈⣀⣠⣾⣅⠀⠑⠂⠤⠌⣩⡇⠀
⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⣺⢁⣞⣉⡴⠟⡀⠀⠀⠀⠁⠸⡅⠀⠈⢷⠈⠏⠙⠀⢹⡛⠀⢉⠀⠀⠀⣀⣀⣼⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡟⢡⠖⣡⡴⠂⣀⣀⣀⣰⣁⣀⣀⣸⠀⠀⠀⠀⠈⠁⠀⠀⠈⠀⣠⠜⠋⣠⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⢿⣿⣿⣷⡟⢋⣥⣖⣉⠀⠈⢁⡀⠤⠚⠿⣷⡦⢀⣠⣀⠢⣄⣀⡠⠔⠋⠁⠀⣼⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠈⠻⣿⣿⢿⣛⣩⠤⠒⠉⠁⠀⠀⠀⠀⠀⠉⠒⢤⡀⠉⠁⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣤⣤⠴⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⠀⠀⠀⠀⠀⢩⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
art_process_hacker_name_1=""" 
 ____ 
(_   )
 / /_ 
(____)
"""
art_process_hacker_name_2="""
 ____    __   
(_   )  /__\  
 / /_  /(__)\ 
(____)(__)(__)
"""
art_process_hacker_name_3="""
 ____    __    _   _ 
(_   )  /__\  ( )_( )
 / /_  /(__)\  ) _ ( 
(____)(__)(__)(_) (_)
"""
art_process_hacker_name_4="""
 ____    __    _   _  ____ 
(_   )  /__\  ( )_( )(_  _)
 / /_  /(__)\  ) _ (  _)(_ 
(____)(__)(__)(_) (_)(____)
"""
art_process_hacker_name_5="""
 ____    __    _   _  ____  ____   
(_   )  /__\  ( )_( )(_  _)(  _ \  
 / /_  /(__)\  ) _ (  _)(_  )(_) ) 
(____)(__)(__)(_) (_)(____)(____/  

"""
art_process_hacker_name_6="""
 ____    __    _   _  ____  ____     _   _ 
(_   )  /__\  ( )_( )(_  _)(  _ \   ( )_( )
 / /_  /(__)\  ) _ (  _)(_  )(_) )   ) _ ( 
(____)(__)(__)(_) (_)(____)(____/   (_) (_)

"""
art_process_hacker_name_7="""
 ____    __    _   _  ____  ____     _   _    __   
(_   )  /__\  ( )_( )(_  _)(  _ \   ( )_( )  /__\  
 / /_  /(__)\  ) _ (  _)(_  )(_) )   ) _ (  /(__)\ 
(____)(__)(__)(_) (_)(____)(____/   (_) (_)(__)(__)

"""
art_process_hacker_name_8="""
 ____    __    _   _  ____  ____     _   _    __    ___ 
(_   )  /__\  ( )_( )(_  _)(  _ \   ( )_( )  /__\  / __)
 / /_  /(__)\  ) _ (  _)(_  )(_) )   ) _ (  /(__)\ \__ 
(____)(__)(__)(_) (_)(____)(____/   (_) (_)(__)(__)(___/

"""
art_process_hacker_name_9="""
 ____    __    _   _  ____  ____     _   _    __    ___    __   
(_   )  /__\  ( )_( )(_  _)(  _ \   ( )_( )  /__\  / __)  /__\  
 / /_  /(__)\  ) _ (  _)(_  )(_) )   ) _ (  /(__)\ \__ \ /(__)\ 
(____)(__)(__)(_) (_)(____)(____/   (_) (_)(__)(__)(___/(__)(__)

"""
art_process_hacker_name_10="""
 ____    __    _   _  ____  ____     _   _    __    ___    __    _  _ 
(_   )  /__\  ( )_( )(_  _)(  _ \   ( )_( )  /__\  / __)  /__\  ( \( )
 / /_  /(__)\  ) _ (  _)(_  )(_) )   ) _ (  /(__)\ \__ \ /(__)\  )  ( 
(____)(__)(__)(_) (_)(____)(____/   (_) (_)(__)(__)(___/(__)(__)(_)\_)

"""
art_process_hacker ="""
    



⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⠶⠶⠶⠶⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠛⠁⠀⠀⠀⠀⠀⠀⠈⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⣠⡴⠞⠛⠉⠉⣩⣍⠉⠉⠛⠳⢦⣄⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⣴⡿⣧⣀⠀⢀⣠⡴⠋⠙⢷⣄⡀⠀⣀⣼⢿⣦⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⡾⠋⣷⠈⠉⠉⠉⠉⠀⠀⠀⠀⠉⠉⠋⠉⠁⣼⠙⢷⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣹⣆⠀⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡟⠀⣰⣏⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠞⠋⠁⠙⢷⣄⠙⢷⣀⠀⠀⠀⠀⠀⠀⢀⡴⠋⢀⡾⠋⠈⠙⠻⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠹⢦⡀⠙⠳⠶⢤⡤⠶⠞⠋⢀⡴⠟⠀⠀⠀⠀⠀⠀⠙⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⢀⣤⣤⣤⣤⣤⣤⣤⣿⣦⣤⣤⣤⣤⣤⣤⣴⣿⣤⣤⣤⣤⣤⣤⣤⡀⠀⠀⠙⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⠏⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⢠⣴⠞⠛⠛⠻⢦⡄⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣿⣿⢶⣄⣠⡶⣦⣿⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⢻⣿⠶⠟⠻⠶⢿⡿⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢾⣄⣹⣦⣀⣀⣴⢟⣠⡶⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣭⣭⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⣀⡴⠞⠋⠙⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣄⣀⠀⠀⢀⣤⣼⣧⣤⣤⣤⣤⣤⣿⣭⣤⣤⣤⣤⣤⣤⣭⣿⣤⣤⣤⣤⣤⣼⣿⣤⣄⠀⠀⣀⣠⡾⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠻⢧⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠼⠟⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀
           _     _     _   _    _                       
          | |   (_)   | | | |  | |                      
  ______ _| |__  _  __| | | |__| | __ _ ___  __ _ _ __  
 |_  / _` | '_ \| |/ _` | |  __  |/ _` / __|/ _` | '_ \ 
  / / (_| | | | | | (_| | | |  | | (_| \__ \ (_| | | | |
 /___\__,_|_| |_|_|\__,_| |_|  |_|\__,_|___/\__,_|_| |_|
⣷⣶⣶⣶⣶⣶⣶⣿⣷⣶⣿⣿⣾⣿⣶⣶⣿⣿⣷⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣷⣷⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣷⣷⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⣶⣿⣿

"""
art_hacker_3="""
⠀⢠⣶⣿⣿⣗⡢⠀⠀⠀⠀⠀⠀⢤⣒⣿⣿⣷⣆⠀⠀
⠀⠋⠉⠉⠙⠻⣿⣷⡄⠀⠀⠀⣴⣿⠿⠛⠉⠉⠉⠃⠀
⠀⠀⢀⡠⢤⣠⣀⡹⡄⠀⠀⠀⡞⣁⣤⣠⠤⡀⠀⠀⠀
⢐⡤⢾⣿⣿⢿⣿⡿⠀⠀⠀⠀⠸⣿⣿⢿⣿⣾⠦⣌⠀
⠁⠀⠀⠀⠉⠈⠀⠀⣸⠀⠀⢰⡀⠀⠈⠈⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⣀⡔⢹⠀⠀⢸⠳⡄⡀⠀⠀⠀⠀⠀⠀
⠸⡦⣤⠤⠒⠋⠘⢠⡸⣀⣀⡸⣠⠘⠉⠓⠠⣤⢤⡞⠀
⠀⢹⡜⢷⣄⠀⣀⣀⣾⡶⢶⣷⣄⣀⡀⢀⣴⢏⡾⠁⠀
⠀⠀⠹⡮⡛⠛⠛⠻⠿⠥⠤⠽⠿⠛⠛⠛⣣⡾⠁⠀⠀
⠀⠀⠀⠙⢄⠁⠀⠀⠀⣄⣀⡄⠀⠀⠀⢁⠞⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠂⠀⠀⠀⢸⣿⠀⠀⠀⠠⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


"""
chinese_text_1="""前面的几位数字通常代表不同的地区或运营商。电话号码的长度和格式在不同的国家和地区可能会有所不
"""
chinese_text_2="""电话号码是用来进行电话通信的数字串。电话号码通常由一系列数字组成，用于拨打电话或发送短信
"""
chinese_text_3="""随着移动电话和互联网的普及，电话号码已经成为现代社会不可或缺的一部分，用于沟通、预约、验证和许多其他用途
"""
chinese_text_4="""电话号码是用来进行电话通信的数字串。电话号码通常由一系列数字组成，用于拨打电话或发送短信
"""
z_sleep_short=0.3
z_sleep_long=1
z_sleep_process=0.1
while True:
    #some animation
    print(art_process_hacker)
    time.sleep(z_sleep_short)
    os.system('cls')
    print(art_process_hacker+chinese_text_1)
    time.sleep(z_sleep_short)
    os.system('cls')
    print(art_process_hacker+chinese_text_1+chinese_text_2)
    time.sleep(z_sleep_short)
    os.system('cls')
    print(art_process_hacker+chinese_text_1+chinese_text_2+chinese_text_3)
    time.sleep(z_sleep_short)
    #os.system('cls')
    #print(art_process_hacker+chinese_text_1+chinese_text_2+chinese_text_3+chinese_text_4)
    #time.sleep(z_sleep_short)
    # Prepare the post message and link
    post_message = input("文本: ")
    post_link = input("關聯: ")
    #some animation
    os.system('cls')
    print(art_hacker_2)
    time.sleep(z_sleep_process)
    os.system('cls')
    print(art_hacker_2)
    print(art_process_hacker_name_1)
    time.sleep(z_sleep_process)
    os.system('cls')
    print(art_hacker_2)
    print(art_process_hacker_name_2)
    time.sleep(z_sleep_process)
    os.system('cls')
    print(art_hacker_2)
    print(art_process_hacker_name_3)
    time.sleep(z_sleep_process)
    os.system('cls')
    print(art_hacker_2)
    print(art_process_hacker_name_4)
    time.sleep(z_sleep_process)
    os.system('cls')
    print(art_hacker_2)
    print(art_process_hacker_name_5)
    time.sleep(z_sleep_process)
    os.system('cls')
    print(art_hacker_2)
    print(art_process_hacker_name_6)
    time.sleep(z_sleep_process)
    os.system('cls')
    print(art_hacker_2)
    print(art_process_hacker_name_7)
    time.sleep(z_sleep_process)
    os.system('cls')
    print(art_hacker_2)
    print(art_process_hacker_name_8)
    time.sleep(z_sleep_process)
    os.system('cls')
    print(art_hacker_2)
    print(art_process_hacker_name_9)
    time.sleep(z_sleep_process)
    os.system('cls')
    print(art_hacker_2)
    print(art_process_hacker_name_10)
    time.sleep(z_sleep_long)
    os.system('cls')
    #loop animation
    print(art_hacker_3)
    time.sleep(2)
    #loop -------------------------------------------------------------------------
    for access_token, page_id in zip(access_tokens, page_ids):
        graph = facebook.GraphAPI(access_token)
        # Prepare the post data
        post_data = {
            "message": post_message,
            "link": post_link
        }
        # Publish the post to the current page
        graph.put_object(page_id, "feed", **post_data)    
        print ("成功"+page_id+"發布完成")
    #end animation
    os.system('cls')
    print(art_process_end_fire)
    time.sleep(z_sleep_long)
    z_exit=input('按 y 退出：')
    if z_exit.lower() =='y':
        break
    else:
        continue

