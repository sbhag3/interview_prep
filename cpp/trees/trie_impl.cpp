class TrieNode {
    private:
        TrieNode* links[26];
        bool end;
    public:
        TrieNode() {
            for (int i = 0; i < 26; i++) {
                links[i] = nullptr;
            }
            end = false;
        }

        bool containsKey(char ch) {
            return links[ch - 'a'] != nullptr;
        }

        TrieNode* get(char ch) {
            return links[ch - 'a'];
        }

        void put(char ch, TrieNode* node) {
            links[ch - 'a'] = node;
        }

        void setEnd() { 
            end = true; 
        }
        bool isEnd() { 
            return end; 
        }
};

class Trie {
public:
    TrieNode* root;
    Trie() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* curr = root;
        for (int i = 0; i < word.length(); i++) {
            char currChar = word[i];
            if (!curr->containsKey(currChar)) {
                curr->put(currChar, new TrieNode());
            }
            curr = curr->get(currChar);
        }
        curr->setEnd();
    }
    
    bool search(string word) {
        TrieNode* curr = root;
        for (int i = 0; i < word.length(); i++) {
            char currChar = word[i];
            if (curr->containsKey(currChar)) {
                curr = curr->get(currChar);
            } else return false;
        }
        return curr != nullptr && curr->isEnd();
    }
    
    bool startsWith(string prefix) {
        TrieNode* curr = root;
        for (int i = 0; i < prefix.length(); i++) {
            char currChar = prefix[i];
            if (curr->containsKey(currChar)) {
                curr = curr->get(currChar);
            } else return false;
        }
        return curr != nullptr;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */