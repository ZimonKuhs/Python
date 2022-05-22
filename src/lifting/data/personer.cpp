#include <string>
#include <vector>

typedef struct Name {
    std::string name;
    std::string *person = nullptr;
} Name;

int main(int argc, char **argv) {

    std::vector<Name> names = {};
    std::string person = "Daniel";

    for(int i = 0; i < 5; ++i) {
        Name name = {
            "Name" + std::to_string(i),
            &person
        };
        names[i] = name;
    }
}
