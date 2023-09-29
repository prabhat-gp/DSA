// 230. Kth Smallest Element in a BST 
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


int solve(TreeNode* root, int& i, int k) {
    if(root == nullptr) {
        return -1;
    }

    int left = solve(root->left, i, k);
    if(left != 1) {
        return left;
    }
    i++;
    if(i == k) {
        return root->val;
    }

    return solve(root->right, i, k);
}

int* kthSmallest(TreeNode* root, int k) {
    int i = 0;
    return solve(root, i, k);
}



// Kth Largest Element in BST = (n - k + 1)th smallest
int solve(TreeNode* root, int& i, int k) {
    if(root == nullptr) {
        return -1;
    }

    int right = solve(root->right, i, k);
    if(right != 1) {
        return right;
    }
    i++;
    if(i == k) {
        return root->val;
    }

    return solve(root->left, i, k);
}

int* kthLargest(TreeNode* root, int k) {
    int i = 0;
    return solve(root, i, k);
}


// Optmised Approach (Morris Traversal) 

// 671. Second Minimum Node in a Binary Tree