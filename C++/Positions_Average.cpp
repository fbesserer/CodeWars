#include <string>
#include <vector>
#include <cmath>
#include <iostream>
#include <sstream>
#include <unordered_map>
#include <chrono>


std::vector<std::string> splitString(const std::string &s)
{
    std::vector<std::string> splitStrings;
    std::string delimiter = ", ";
    int startIndex = 0;
    int endIndex = 0;
    while ((endIndex = s.find(delimiter, startIndex)) < s.size())
    {
        std::string val = s.substr(startIndex, endIndex - startIndex);
        splitStrings.emplace_back(val);
        startIndex = endIndex + delimiter.size();
    }
    if (startIndex < s.size())
    {
        std::string val = s.substr(startIndex, s.size() - startIndex);
        splitStrings.emplace_back(val);
    }
    return splitStrings;
}

std::vector<std::string> shorterSplitString(const std::string &s)
{ // optimized version if all substrings are known to have the same length
    std::vector<std::string> vec;
    int delimiter = s.find(',');
    for (int i = 0; i < s.size(); i += delimiter + 2)
    {/*delimiter searches only once from the beginning of the string since all substrings are supposed to be the same size and returns the length of the entry.
       after the last substring i will be greater than s.size() since current i size + delimiter size + 2 > s.size()*/
        vec.push_back(s.substr(i,delimiter)); // substr(start, length)
    }
    return vec;

}


double posAverage(const std::string &s)
{
	auto splits = shorterSplitString(s);
    int duplicates = 0;
    std::unordered_map<int, int> hashtable;
    int n = splits.size();
    for (int i = 0; i < splits[0].size(); i++)
    {
        for (auto entry : splits) 
        {
            hashtable.find(entry[i]) != hashtable.end() ? hashtable[entry[i]]++ : hashtable[entry[i]] = 1;
        }
        for (auto values : hashtable)
        {
            duplicates += (values.second * (values.second -1) / 2);
        }
        hashtable.clear();
    }
    int wordlength = splits[0].size();
    return duplicates / (n * (n-1) / 2. * wordlength) * 100.;
}


int main() {
    std::string assertFuzzy = ("466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096");
    auto start = std::chrono::high_resolution_clock::now();
    auto result = posAverage(assertFuzzy);
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);
    std::cout << "Time elapsed: " << duration.count() << " nanos\n";
    std::cout << result;
}