# Changelog

## [Unreleased]
- Placeholder for upcoming changes.

## [1.0.0] - 2025-09-02
- Initial version of ACEest Fitness DevOps project.
- Updated ReadME.md
- Added requirements.txt

## [1.0.1] - 2025-09-02
- Added ci.yml. Integrated github workflow
- Dockerized the application
- Created flask_api.py to run app in Flask

## [1.0.2] - 2025-09-02
- Updated ci.yml to trigger only on PR merge

## [1.0.3] - 2025-09-02
- Added pytest for flask_api.py
- Enabled pytest in ci.yml
- Added store.py logic for data storage in memory

## [1.0.4] - 2025-09-02
- Update github workflow to follow different run/build pattern for main and for feature-branch

## [1.0.5] - 2025-09-03
- Added falsk_web.py for application UI
- Added UI folder with html files for look and feel of the application
- Fix falsk_api.py import of store

## [1.0.6] - 2025-09-03
-Added Dockerfile.Web to push UI image to docker hub through CI.

## [1.0.7] - 2025-09-03
- Update CI to push Images of API and Web to Docker Hub
