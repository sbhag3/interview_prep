class LRUCache {
public:
    struct Node {
        int key;
        int val;
        Node* next;
        Node* prev;
        Node(int key, int val) : key(key), val(val), next(nullptr), prev(nullptr) {}
    };

    int capacity;
    unordered_map<int, Node*> map;
    Node* head = new Node(-1, -1);
    Node* tail = new Node(-1, -1);

    LRUCache(int capacity) {
        this->capacity = capacity;
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if (map.find(key) == map.end()) return -1;
        Node* node = map[key];
        remove(node);
        add(node);
        return node->val;
    }
    
    void put(int key, int value) {
        if (map.find(key) != map.end()) {
            Node* old = map[key];
            remove(old);
        }
        Node* newNode = new Node(key, value);
        map[key] = newNode;
        add(newNode);
        if (map.size() > capacity) {
            Node* deleted = head->next;
            remove(deleted);
            map.erase(deleted->key);
        }
    }

    void add(Node* node) {
        Node* prevEnd = tail->prev;
        prevEnd->next = node;
        node->prev = prevEnd;
        node->next = tail;
        tail->prev = node;
    }

    void remove(Node* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */