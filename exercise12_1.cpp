#include <sstream>

int solve(std::string filename, int k)
{
    std::stringstream ss;
    ss << "tail -n " << k << " " << filename;
    return std::system(ss.str().c_str());
}

int main()
{
    std::string filename{"exercise12_1.cpp"};
    int k{5};
    return solve(filename, k);
}
