// 1441. Build an Array with Stack Operations 

vector<string> buildArray(vector<int>& target, int n) {
    vector<string> temp;
    int ptr = 0;
    int curr = 1;

    while(ptr < target.size()) {
        if(target[ptr] == curr) {
            temp.push_back("Push");
            ptr++;
        } else {
            temp.push_back("Push");
            temp.push_back("Pop");
        }
        curr++;
    }
    return temp;
}