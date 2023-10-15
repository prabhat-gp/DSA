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

// Largest BST
#include <climits>
#include <algorithm>

struct subTreeInfo {
    int size;
    int minVal;
    int maxVal;
    bool isBST;
};

subTreeInfo solve(TreeNode* root, int& maxSize) {
    if(root == nullptr)
        return {0, INT_MAX, INT_MIN, true};

    subTreeInfo left = solve(root->left, maxSize);
    subTreeInfo right = solve(root->right, maxSize);

    if(left.isBST && right.isBST && root->val > left.maxVal && root->val < right.minVal) {
        int subtree_size = 1 + left.size + right.size;
        maxSize = max(maxSize, subtree_size);
        return {
            subtree_size,
            min(root->val, left.minVal),
            max(root->val, right.maxVal),
            true
        };
    } else {
        return {0, 0, 0, false};
    }
}

int largestBST(TreeNode* root) {
    int maxSize = 0;
    solve(root, maxSize);
    return maxSize;
}

// Preorder to Postorder 
TreeNode* solve(TreeNode* root, int v) {
    if (root == nullptr) 
        return newNode(v);
    if (v < root->data) 
        root->left = solve(root->left, v);
    else 
        root->right = solve(root->right, v);

    return root;
}

TreeNode* postOrder(int pre[], int size) {
    TreeNode* root = nullptr;
    for(int i = 0; i < size; i++) {
        root = solve(root, pre[i]);
    }

    return root;
}


// Maximum difference between node and its ancestor
// Maximum path sum from any node
// Maximum sum leaf to root path
// Delete nodes greater than k
// BST to greater sum tree

