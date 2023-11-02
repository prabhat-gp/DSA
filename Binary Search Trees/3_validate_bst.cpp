// 98. Valiate Binary Search Tree 

// Properties of BST 
// * For every node, left subtree has values less that root and right subtree has values greater than root. 
// * Inorder Traversal is sorted


struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int val) {
        this->val = val;
        this->left = NULL;
        this->right = NULL;
    }
}


bool solve(TreeNode* root, int minVal, int maxVal) {
    if(root == nullptr) return true;

    if(root->val > min && root->val < max) {
        bool left = solve(root->left, min, root->val);
        bool right = solve(root->right, root->val, max);
        return left && right;
    }

    return false;
}

bool isValidBST(TreeNode* root) {
    return solve(root, INT_MIN, INT_MAX);
}



// 501. Find Mode in Binary Search Tree 
void inorderTraversal(TreeNode* root, vector<int>& res) {
    if (root == NULL) return;

    inorderTraversal(root->left, res);
    res.push_back(root->val);
    inorderTraversal(root->right, res);
}

vector<int> findMode(TreeNode* root) {
    vector<int> res;
    inorderTraversal(root, res);
    int mx = INT_MIN;
     unordered_map<int, int> map;

    for (int i = 0; i < res.size(); i++) {
        map[res[i]]++;
        mx = max(map[res[i]], mx);
    }
    vector<int> temp;
    for (auto it : map) {
        if (it.second == mx)
            temp.push_back(it.first);
    }
    return temp;
}



// Median in BST 
void inorder(Node* root, vector<int> &ans) {
    if(root == NULL) return;
    
    inorder(root->left,ans);
    ans.push_back(root->data);
    inorder(root->right,ans);
}

float findMedian(struct Node *root) {
    vector<int> temp;
    inorder(root, temp);
    float ans;
    int size = temp.size();
    if(size % 2 != 0) {
        int index = (size + 1) / 2;
        ans = temp[index - 1];
    } else {
        int a = size / 2;
        int b = (size / 2) + 1;
        ans = (temp[a - 1] + temp[b - 1]) / 2.0;
    }
    return ans;
}



// 1361. Validate Binary Tree Nodes
#include <vector>
#include <deque>
#include <unordered_set>

bool validateBinaryTreeNodes(int n, vector<int>& leftChild, vector<int>& rightChild) {
    int root = 0;
    unordered_set<int> childrenNodes;

    for(int i = 0; i < n; i++) {
        if(leftChild[i] != -1)
            childrenNodes.insert(leftChild[i]);
        if(rightChild[i] != -1)
            childrenNodes.insert(rightChild[i]);
    }

    for(int i = 0; i < n; i++) {
        if(childrenNodes.find(i) == childrenNodes.end())
            root = i;
    }

    unordered_set<int> visited;
    deque<int> dq;
    dq.push_back(root);

    while(!dq.empty()) {
        int curr = dq.front();
        dq.pop_front();

        if(visited.find(curr) != visited.end())
            return false;
        
        visited.insert(curr);

        if(leftChild[curr] != -1)
            dq.push_back(leftChild[curr]);
        if(rightChild[curr] != -1)
            dq.push_back(rightChild[curr]);
    }

    return visited.size() == n;
}


// LCA in BST 
// Find common nodes in two BSTs 