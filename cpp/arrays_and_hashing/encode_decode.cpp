class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string ret;
        for (string s : strs) {
            ret += to_string(s.size()) + "-" + s;
        }
        return ret;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> ret;
        int start = 0;
        int end = s.find("-");
        while (end != string::npos) {
            int size = stoi(s.substr(start, end - start));
            ret.push_back(s.substr(end+1, size));
            start = end+size+1;
            end = s.find("-", start);
        }
        return ret;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));