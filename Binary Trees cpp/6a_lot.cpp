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

// 102. Binary Tree Level Order Traversal
vector<int> levelOrderTraversal(TreeNode* root) {
    if (root == nullptr) return {}

    vector<int> res;
    queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
        TreeNode* curr = q.front();
        q.pop();
        res.push_back(curr->val);

        if (curr->left) {
            q.push(curr->left);
        }

        if (curr->right) {
            q.push(curr->right);
        }
    }

    return res;
}



// 107. Binary Tree Level Order Traversal (Reverse LOT)
vector<int> reverseLevelOrder(TreeNode* root) {
    if (root == nullptr) return {};

    queue<TreeNode*> qu;
    qu.push(root);
    vector<int> ans;

    while (!qu.empty()) {
        vector<int> v;
        int size = qu.size();

        for (int i = 0; i < size; i++) {
            TreeNode* curr = qu.front();
            qu.pop();
            v.push_back(curr->val);

            if (curr->left) {
                qu.push(curr->left);
            }

            if (curr->right) {
                qu.push(curr->right);
            }
        }
        ans.insert(ans.begin(), v.begin(), v.end());
    }
    return ans;
}



// 515. Find Largest Value in Each Tree Row
vector<int> largestValues(TreeNode* root) {
    if (root == nullptr) return {};

    vector<int> res; 
    queue<TreeNode*> qu;
    qu.push(root);

    while (!qu.empty()) {
        int n = qu.size();
        int maxVal = INT_MIN;

        for (int i = 0; i < n; i++) {
            TreeNode* curr = qu.front();
            qu.pop();
            maxVal = max(maxVal, curr->val);

            if (curr->left) qu.push(curr->left);
            if (curr->right) qu.push(curr->right);
        }
        res.push_back(maxVal);
    }
    return res;
}




// 129. Sum Root to Leaf Numbers 
// Morris Traversal Possible 
int sumNumbers(TreeNode* root) {
    int sum = 0;
    queue<pair<TreeNode*, int>> qu; 
    qu.push(make_pair(root, 0)); 

    while (!qu.empty()) {
        pair<TreeNode*, int> temp = qu.front();
        qu.pop();
        TreeNode* curr = temp.first;
        int n = temp.second * 10 + curr->val; 

        if (curr->left) 
            qu.push(make_pair(curr->left, n));

        if (curr->right) 
            qu.push(make_pair(curr->right, n));

        if (!curr->left && !curr->right) 
            sum += n;
    }
    return sum;
}



// 637. Average of Levels in Binary Tree
vector<double> averageOfLevels(TreeNode* root) {
    if (root == nullptr) return {};

    vector<double> temp;
    queue<TreeNode*> qu;
    qu.push(root);
    
    while (!qu.empty()) {
        int levelSize = qu.size();
        double levelSum = 0.0;
        
        for (int i = 0; i < levelSize; i++) {
            TreeNode* curr = qu.front();
            qu.pop();
            levelSum += curr->val;
            
            if (curr->left) 
                qu.push(curr->left);
            
            if (curr->right) 
                qu.push(curr->right);
            
        }
        double levelAverage = levelSum / levelSize;
        temp.push_back(levelAverage);
    }
    return temp;
}



// 257. Binary Tree Paths 
// 1022. Sum to Root to Leaf Binary Numbers 
