#include <sstream>

int solve(std::string filename, int k)
{
    std::stringstream ss;
    ss << "tail -n " << k << " " << filename;
    return std::system(ss.str().c_str());
}
