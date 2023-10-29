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



// 958. Check Completeness of a Binary Tree
bool isCompleteTree(TreeNode* root) {
    if (root == nullptr) {
        return true;
    }

    queue<TreeNode*> qu;
    qu.push(root);
    bool gap = false;

    while (!qu.empty()) {
        TreeNode* curr = qu.front();
        qu.pop();

        if (curr == nullptr) {
            gap = true;
            continue;
        }

        qu.push(curr->left);
        qu.push(curr->right);

        if (gap) {
            return false;
        }
    }

    return true;
}



// 1161. Maximum Level Sum of Binary Tree  (Maximum Sum or Maximum Level of Binary Tree (both))
int maxLevelSum(TreeNode* root) {
    if (root == nullptr) {
        return 0;
    }

    queue<TreeNode*> qu;
    qu.push(root);
    int level = 1;
    int maxLevel = 1;
    int maxSum = root->data;

    while (!qu.empty()) {
        int currSum = 0;
        int currLevel = qu.size();

        for (int i = 0; i < currLevel; i++) {
            TreeNode* curr = qu.front();
            qu.pop();
            currSum += curr->data;

            if (curr->left) {
                qu.push(curr->left);
            }

            if (curr->right) {
                qu.push(curr->right);
            }
        }
        if (currSum > maxSum) {
            maxSum = currSum;
            maxLevel = level;
        }
        level++;
    }
    return maxLevel;
}



// 2583. kth Largest Sum in Binary Tree
int kthLargestLevelSum(TreeNode* root, int k) {
    if (root == nullptr) {
        return -1;
    }

    queue<TreeNode*> qu;
    qu.push(root);
    vector<int> levelSum;

    while (!qu.empty()) {
        int currSum = 0;
        int currLevel = qu.size();

        for (int i = 0; i < currLevel; i++) {
            TreeNode* curr = qu.front();
            qu.pop();
            currSum += curr->data;

            if (curr->left) {
                qu.push(curr->left);
            }

            if (curr->right) {
                qu.push(curr->right);
            }
        }

        levelSum.push_back(currSum);
    }

    sort(levelSum.rbegin(), levelSum.rend());

    if (k <= levelSum.size()) {
        return levelSum[k - 1];
    }

    return -1;
}

// Connect Nodes at Same Level 
void connect(TreeNode* root) {
    queue<TreeNode*> qu;
    qu.push(root);

    while(!qu.empty()) {
        int size = qu.size();

        for(int i = 0; i < size; i++) {
            TreeNode* curr = qu.front();
            qu.pop();

            if(!qu.empty() && i < size - 1)
                curr->nextRight = qu.front();
            else    
                curr->nextRight = nullptr
            
            if(curr->left)
                qu.push(curr->left)
            if(curr->right)
                qu.push(curr->right)
        }
    }
}