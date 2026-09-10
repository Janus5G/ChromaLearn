#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"; VERSION=0.4.5; PKGROOT="$ROOT/build/chromalearn_${VERSION}_all"; DIST="$ROOT/dist"
rm -rf "$ROOT/build" "$DIST"; mkdir -p "$PKGROOT/DEBIAN" "$PKGROOT/usr/lib/chromalearn" "$PKGROOT/usr/bin" "$PKGROOT/usr/share/applications" "$PKGROOT/usr/share/icons/hicolor/scalable/apps" "$PKGROOT/usr/share/doc/chromalearn" "$PKGROOT/usr/share/chromalearn" "$PKGROOT/etc/chromalearn" "$PKGROOT/var/lib/chromalearn/profiles" "$DIST"
cp "$ROOT/src/chromalearn/"*.py "$PKGROOT/usr/lib/chromalearn/"; cp "$ROOT/src/chromalearn/config.json" "$PKGROOT/etc/chromalearn/config.json"; cp "$ROOT/examples/matematik-7.json" "$PKGROOT/var/lib/chromalearn/profiles/"; cp "$ROOT/packaging/chromalearn.desktop" "$PKGROOT/usr/share/applications/";cp "$ROOT/packaging/chromalearn.svg" "$PKGROOT/usr/share/icons/hicolor/scalable/apps/";cp "$ROOT/LICENSE" "$ROOT/README.md" "$ROOT/CHANGELOG.md" "$ROOT/docs/"*.md "$PKGROOT/usr/share/doc/chromalearn/"
cat > "$PKGROOT/usr/bin/chromalearn" <<'EOF'
#!/usr/bin/env bash
exec python3 /usr/lib/chromalearn/app.py "$@"
EOF
cat > "$PKGROOT/usr/bin/chromalearn-export-source" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
DEST="${1:-$HOME/chromalearn-dev}"
if [ -e "$DEST" ]; then echo "Destination exists: $DEST" >&2; exit 2; fi
cp -a /usr/share/chromalearn/developer-repo "$DEST"
chmod -R u+rwX "$DEST"
echo "ChromaLearn developer repository copied to: $DEST"
echo "Next: cd '$DEST' && git status"
EOF
cp "$ROOT/packaging/chromalearn-privacy-scan" "$PKGROOT/usr/bin/chromalearn-privacy-scan"
cp "$ROOT/packaging/chromalearn-translate" "$PKGROOT/usr/bin/chromalearn-translate"
chmod 0755 "$PKGROOT/usr/bin/chromalearn" "$PKGROOT/usr/bin/chromalearn-export-source" "$PKGROOT/usr/lib/chromalearn/app.py" "$PKGROOT/usr/bin/chromalearn-privacy-scan" "$PKGROOT/usr/bin/chromalearn-translate"
# Embed a complete Git repository, excluding current build artifacts and any caller repository metadata.
DEV="$PKGROOT/usr/share/chromalearn/developer-repo";mkdir -p "$DEV"; tar --exclude='./build' --exclude='./dist' --exclude='./.git' --exclude='./.pytest_cache' --exclude='*/.pytest_cache' --exclude='__pycache__' -C "$ROOT" -cf - . | tar -C "$DEV" -xf -
if command -v git >/dev/null; then
 git -C "$DEV" init -q; git -C "$DEV" add .; git -C "$DEV" -c user.name='Janus Rokkjær' -c user.email='janusdkbiz@gmail.com' commit -q -m 'ChromaLearn AI 0.4.5 source release'
fi
cat > "$PKGROOT/DEBIAN/control" <<EOF
Package: chromalearn
Version: $VERSION
Section: education
Priority: optional
Architecture: all
Depends: python3 (>= 3.10)
Recommends: git
Maintainer: Janus Rokkjær
Description: Open-source pædagogisk AI-lag til skoler
 Rolleopdelt elev-, lærer- og IT-administration med konfigurerbar
 OpenAI-kompatibel inference-backend og indbygget Git developer-repository.
EOF
cat > "$PKGROOT/DEBIAN/conffiles" <<'EOF'
/etc/chromalearn/config.json
EOF
cat > "$PKGROOT/DEBIAN/postinst" <<'EOF'
#!/bin/sh
set -e
getent group chromalearn-teacher >/dev/null || addgroup --system chromalearn-teacher >/dev/null
getent group chromalearn-admin >/dev/null || addgroup --system chromalearn-admin >/dev/null
chown root:chromalearn-admin /etc/chromalearn/config.json || true
chmod 0660 /etc/chromalearn/config.json || true
mkdir -p /var/lib/chromalearn/profiles
chown root:chromalearn-teacher /var/lib/chromalearn/profiles || true
chmod 2770 /var/lib/chromalearn/profiles || true
find /var/lib/chromalearn/profiles -type f -name '*.json' -exec chown root:chromalearn-teacher {} \; -exec chmod 0660 {} \; || true
exit 0
EOF
chmod 0755 "$PKGROOT/DEBIAN/postinst"
find "$PKGROOT" -type d -exec chmod 0755 {} +; chmod 2770 "$PKGROOT/var/lib/chromalearn/profiles"; find "$PKGROOT" -type f -not -path '*/DEBIAN/postinst' -not -path '*/usr/bin/*' -not -path '*/usr/lib/chromalearn/app.py' -exec chmod 0644 {} +; chmod 0755 "$PKGROOT/DEBIAN/postinst" "$PKGROOT/usr/bin/"* "$PKGROOT/usr/lib/chromalearn/app.py"
# Preserve executable bits inside the embedded developer Git repository.
chmod 0755 "$DEV/build_deb.sh" "$DEV/src/chromalearn/app.py" "$DEV/packaging/chromalearn-privacy-scan" "$DEV/packaging/chromalearn-translate"
chmod 0755 "$PKGROOT" "$PKGROOT/DEBIAN"
chmod g-s "$PKGROOT" "$PKGROOT/DEBIAN"
dpkg-deb --root-owner-group --build "$PKGROOT" "$DIST/chromalearn_${VERSION}_all.deb"
echo "$DIST/chromalearn_${VERSION}_all.deb"
