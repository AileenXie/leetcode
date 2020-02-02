# leetcode

## 加减乘除运算
002_add_two_numbers.py  # 链表数字做加法
029_divide_two_integers*.py  # 实现整除
050_pow.py  # 实现乘幂
066_plus_one.py  # 数列末尾值+1
069_sqrt.py  # 实现开根号

### sum
001_two_sum.py  # 求list中能加和成指定值的两个位置
015_3_sum**.py  # 求list中能加和成0的三个值


## 数列
004_median_of_two_sorted_arrays.py  # 两个有序数列找中位数
007_reverse_interger.py  # 数字倒叙输出
033_search_in_rotated_sorted_array.py  # 旋转排序的数列中查找
034_find_first_and_last_position_of_element_in_sorted_array.py  # 查找第一次出现和最后一次出现的位置
041_first_missing_positive.py  # 未排序数列找到缺失的最小正整数
046_permutations.py  # 找到数列的所有排列组合
056_merge_intervals.py  # 融合区间范围
### 去重
026_remove_duplicates_from_sorted_array.py  # 有序数列去重后长度
### 子序列
053_maximum_subarray*.py  # 找到加和最大的子序列（滚雪球法）
078_subsets*.py  # 列出序列部分/全部数字的所有排列组合
### 排序
075_sort_colors.py  # 冒泡排序


## 回文
009_palindrome_number.py  # 判断数字是否是回文数字（可能负数）
125_valid_palindrome.py  # 忽略符号判断字符串中字母是否是回文
005_longest_palindromic_substring.py  # 最长回文
131_palindrome_partitioning*.py  # 字符串切分成回文组合
132_palindrome_partition_II**.py  # 字符串切分成回文的最小切割次数

## 字符串
### 组合/合并
049_group_anagrams*.py  # 相同字母组成的字符串重新组队
088_merge_sorted_array.py  #合并数列
### 子串
003_longest_substring_without_repeating_characters.py  # 最长无重复子串长度
005_longest_palindromic_substring.py  # 最长回文
028_implement_strStr().py  # 找出子串最早出现的位置
076_minimum_window_substring_.py  # 包含子串全部字母的最小窗口
### 字符空间布局
006_zigzag_conversion.py  # 竖Z型布局按行输出字母
### 字符匹配
010_regular_expression_matching***.py  # 正则匹配（.匹配任意一个字符，*匹配0个或多个前一字符）
044_wildcard_matching.py  # 正则匹配（？匹配任意一个字符，*匹配0个或多个任意字符）
#### 括号匹配
020_valid_parentheses.py  # 判断括号合法性
022_generate_parentheses.py  # 生成合法括号组合


## 字符&数列转换/翻译
008_string_to_integer.py  # 字符串转数字
013_roman_to_integer.py  # 罗马字符转数字
017_Letter_Combinations_of_a_Phone_Number.py  # 九宫格数字转字母组合list
038_count_and_say.py  # 数字 转 "个数+数字"表达
091_decode_ways.py  # 数字-字母编码（递归+记忆搜索）
127_word_ladder**.py  # 字梯，一个字母一个字母变，从startWord到endWord


## 图片化/实例化应用
011_container_with_most_water.py  # 找两个位置获得最大盛水量
036_valid_sudoku.py  # 数独有效性判断
042_trapping_rain_water.py  # 收集雨水（所有位置）
048_rotate_image.py  # 旋转矩阵
054_spiral_matrix.py  # 顺时针输出矩阵
055_jump_game.py  # 判断能否跳到最后
062_unique_paths.py  # 网格起点-终点路径数
070_climbing_stairs.py  # 爬梯子（叶子节点计数+记忆搜索）
079_word_search_.py  # 判断单词是否连在字母矩阵中
118_pascals_triangle.py  # passcal三角
130_surrounded_regions.py  # XO感染区域
134_gas_station*.py  # 加油站，（正向求和，逆向反推）
### 股票
121_best_time_to_buy_and_sell_stock.py
122_best_time_to_buy_and_sell_stock_II.py


## 链表
019_remove_nth_node_from_end_of_list.py  # 移除链表倒数第n个元素
021_merged_two_sorted_lists.py  # 合并两个有序链表
（088_merge_sorted_array.py #合并数列）
023_merge_k_sorted_lists.py  # 合并k个有序链表

## 树
### 二叉树
094_binary_tree_inorder_traversal.py  # 迭代/递归中序遍历

098_validate_binary_search_tree.py  # 判断搜索二叉树
101_symmetric_tree.py  # 判断对称二叉树（中序遍历+收尾数字&层数对比）

102_binary_tree_level_order_traversal.py  # 按层遍历
103_binary_tree_zigzag_level_order_traversal.py  # 在102基础上加了方向
104_maximum_depth_of_binary_tree.py  # 类似102，不记录节点值，只记录层数

105_construct_binary_tree_from_preorder_and_inorder_traversal*.py  # 前序+中序 建树
108_convert_sorted_array_to_binary_search_tree*.py  # 有序序列建立二叉平衡树
116_populating_next_right_pointers_in_each_node**.py  # 完全二叉树构建next指针

124_binary_tree_maximum_path_sum**.py  # 最大子树之和