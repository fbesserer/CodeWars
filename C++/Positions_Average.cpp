#include <string>
#include <vector>
#include <cmath>
#include <iostream>
#include <sstream>

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


double posAverage(const std::string &s)
{
	auto substrings = splitString(s);
    for(int i = 0; i < substrings.size(); i++) 
    {
        std::cout << substrings[i] << "\n";
    }
    return 0.2;
}


int main() {
    std::string assertFuzzy = ("466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096");
    auto result = posAverage(assertFuzzy);
    std::cout << result;
}