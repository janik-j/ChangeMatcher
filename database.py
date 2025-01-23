# database.py
from models import ResearchGroupIndex, ResearchPaperIndex, StartupIndex
from utils import embed_text
import numpy as np

class Database:
    def __init__(self, group_index_path, group_data_path, paper_index_path, paper_data_path, startup_index_path, startup_data_path):
        self.group_index = ResearchGroupIndex(group_index_path, group_data_path)
        self.paper_index = ResearchPaperIndex(paper_index_path, paper_data_path)
        self.startup_index = StartupIndex(startup_index_path, startup_data_path)
        self.groups = self.group_index.data
        self.papers = self.paper_index.data
        self.startups = self.startup_index.data
        # Assuming startups have projects stored within them or a separate file
        self.startups_projects = self.load_projects("data/startup_projects.json")

    def load_projects(self, projects_path):
        import json
        with open(projects_path, 'r') as f:
            return json.load(f)

    def get_relevant_groups(self, query, top_k=3):
        query_embedding = embed_text(query)
        D, I = self.group_index.index.search(np.array([query_embedding], dtype=np.float32), top_k)
        return [self.groups[i] for i in I[0]]

    def get_relevant_papers(self, groups, query, top_k=2):
        retrieved_papers = []
        for group in groups:
            for paper_id in group.get("paper_ids", []):
                paper = next((p for p in self.papers if p['id'] == paper_id), None)
                if paper:
                    retrieved_papers.append(paper)
        # Score papers based on query similarity
        query_emb = embed_text(query)
        scored_papers = []
        for paper in retrieved_papers:
            paper_emb = embed_text(paper['abstract'])
            score = np.dot(query_emb, paper_emb) / (np.linalg.norm(query_emb) * np.linalg.norm(paper_emb))
            scored_papers.append((score, paper))
        # Sort by score
        scored_papers.sort(key=lambda x: x[0], reverse=True)
        return [paper for _, paper in scored_papers[:top_k]]

    def get_relevant_startups(self, query, top_k=3):
        query_embedding = embed_text(query)
        D, I = self.startup_index.index.search(np.array([query_embedding], dtype=np.float32), top_k)
        return [self.startups[i] for i in I[0]]

    def get_relevant_projects(self, startups, query, top_k=2):
        retrieved_projects = []
        for startup in startups:
            for project_id in startup.get("project_ids", []):
                project = next((p for p in self.startups_projects if p['id'] == project_id), None)
                if project:
                    retrieved_projects.append(project)
        # Score projects based on query similarity
        query_emb = embed_text(query)
        scored_projects = []
        for project in retrieved_projects:
            project_emb = embed_text(project['description'])
            score = np.dot(query_emb, project_emb) / (np.linalg.norm(query_emb) * np.linalg.norm(project_emb))
            scored_projects.append((score, project))
        # Sort by score
        scored_projects.sort(key=lambda x: x[0], reverse=True)
        return [project for _, project in scored_projects[:top_k]]