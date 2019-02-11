#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kolourpaint
Version  : 18.12.2
Release  : 3
URL      : https://download.kde.org/stable/applications/18.12.2/src/kolourpaint-18.12.2.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.2/src/kolourpaint-18.12.2.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.2/src/kolourpaint-18.12.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 LGPL-2.0
Requires: kolourpaint-bin = %{version}-%{release}
Requires: kolourpaint-data = %{version}-%{release}
Requires: kolourpaint-lib = %{version}-%{release}
Requires: kolourpaint-license = %{version}-%{release}
Requires: kolourpaint-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde

%description
http://www.kolourpaint.org/
For licensing and warranty information, read COPYING.
For known problems with this release of KolourPaint, read BUGS.
For what changes have been made, read NEWS.
For developer information, checkout branches/kolourpaint/control/.

%package bin
Summary: bin components for the kolourpaint package.
Group: Binaries
Requires: kolourpaint-data = %{version}-%{release}
Requires: kolourpaint-license = %{version}-%{release}

%description bin
bin components for the kolourpaint package.


%package data
Summary: data components for the kolourpaint package.
Group: Data

%description data
data components for the kolourpaint package.


%package dev
Summary: dev components for the kolourpaint package.
Group: Development
Requires: kolourpaint-lib = %{version}-%{release}
Requires: kolourpaint-bin = %{version}-%{release}
Requires: kolourpaint-data = %{version}-%{release}
Provides: kolourpaint-devel = %{version}-%{release}

%description dev
dev components for the kolourpaint package.


%package doc
Summary: doc components for the kolourpaint package.
Group: Documentation

%description doc
doc components for the kolourpaint package.


%package lib
Summary: lib components for the kolourpaint package.
Group: Libraries
Requires: kolourpaint-data = %{version}-%{release}
Requires: kolourpaint-license = %{version}-%{release}

%description lib
lib components for the kolourpaint package.


%package license
Summary: license components for the kolourpaint package.
Group: Default

%description license
license components for the kolourpaint package.


%package locales
Summary: locales components for the kolourpaint package.
Group: Default

%description locales
locales components for the kolourpaint package.


%prep
%setup -q -n kolourpaint-18.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549889113
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1549889113
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kolourpaint
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/kolourpaint/COPYING.DOC
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kolourpaint/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang kolourpaint

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kolourpaint

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kolourpaint.desktop
/usr/share/icons/hicolor/16x16/apps/kolourpaint.png
/usr/share/icons/hicolor/22x22/apps/kolourpaint.png
/usr/share/icons/hicolor/32x32/apps/kolourpaint.png
/usr/share/icons/hicolor/48x48/apps/kolourpaint.png
/usr/share/icons/hicolor/scalable/apps/kolourpaint.svgz
/usr/share/kolourpaint/icons/hicolor/16x16/actions/tool_brush.png
/usr/share/kolourpaint/icons/hicolor/16x16/actions/tool_color_eraser.png
/usr/share/kolourpaint/icons/hicolor/16x16/actions/tool_color_picker.png
/usr/share/kolourpaint/icons/hicolor/16x16/actions/tool_curve.png
/usr/share/kolourpaint/icons/hicolor/16x16/actions/tool_ellipse.png
/usr/share/kolourpaint/icons/hicolor/16x16/actions/tool_elliptical_selection.png
/usr/share/kolourpaint/icons/hicolor/16x16/actions/tool_eraser.png
/usr/share/kolourpaint/icons/hicolor/16x16/actions/tool_flood_fill.png
/usr/share/kolourpaint/icons/hicolor/16x16/actions/tool_free_form_selection.png
/usr/share/kolourpaint/icons/hicolor/16x16/actions/tool_line.png
/usr/share/kolourpaint/icons/hicolor/16x16/actions/tool_pen.png
/usr/share/kolourpaint/icons/hicolor/16x16/actions/tool_polygon.png
/usr/share/kolourpaint/icons/hicolor/16x16/actions/tool_polyline.png
/usr/share/kolourpaint/icons/hicolor/16x16/actions/tool_rect_selection.png
/usr/share/kolourpaint/icons/hicolor/16x16/actions/tool_rectangle.png
/usr/share/kolourpaint/icons/hicolor/16x16/actions/tool_rounded_rectangle.png
/usr/share/kolourpaint/icons/hicolor/16x16/actions/tool_spraycan.png
/usr/share/kolourpaint/icons/hicolor/16x16/actions/tool_text.png
/usr/share/kolourpaint/icons/hicolor/22x22/actions/tool_brush.png
/usr/share/kolourpaint/icons/hicolor/22x22/actions/tool_color_eraser.png
/usr/share/kolourpaint/icons/hicolor/22x22/actions/tool_color_picker.png
/usr/share/kolourpaint/icons/hicolor/22x22/actions/tool_curve.png
/usr/share/kolourpaint/icons/hicolor/22x22/actions/tool_ellipse.png
/usr/share/kolourpaint/icons/hicolor/22x22/actions/tool_elliptical_selection.png
/usr/share/kolourpaint/icons/hicolor/22x22/actions/tool_eraser.png
/usr/share/kolourpaint/icons/hicolor/22x22/actions/tool_flood_fill.png
/usr/share/kolourpaint/icons/hicolor/22x22/actions/tool_free_form_selection.png
/usr/share/kolourpaint/icons/hicolor/22x22/actions/tool_line.png
/usr/share/kolourpaint/icons/hicolor/22x22/actions/tool_pen.png
/usr/share/kolourpaint/icons/hicolor/22x22/actions/tool_polygon.png
/usr/share/kolourpaint/icons/hicolor/22x22/actions/tool_polyline.png
/usr/share/kolourpaint/icons/hicolor/22x22/actions/tool_rect_selection.png
/usr/share/kolourpaint/icons/hicolor/22x22/actions/tool_rectangle.png
/usr/share/kolourpaint/icons/hicolor/22x22/actions/tool_rounded_rectangle.png
/usr/share/kolourpaint/icons/hicolor/22x22/actions/tool_spraycan.png
/usr/share/kolourpaint/icons/hicolor/22x22/actions/tool_text.png
/usr/share/kolourpaint/icons/hicolor/32x32/actions/tool_brush.png
/usr/share/kolourpaint/icons/hicolor/32x32/actions/tool_color_eraser.png
/usr/share/kolourpaint/icons/hicolor/32x32/actions/tool_color_picker.png
/usr/share/kolourpaint/icons/hicolor/32x32/actions/tool_curve.png
/usr/share/kolourpaint/icons/hicolor/32x32/actions/tool_ellipse.png
/usr/share/kolourpaint/icons/hicolor/32x32/actions/tool_elliptical_selection.png
/usr/share/kolourpaint/icons/hicolor/32x32/actions/tool_eraser.png
/usr/share/kolourpaint/icons/hicolor/32x32/actions/tool_flood_fill.png
/usr/share/kolourpaint/icons/hicolor/32x32/actions/tool_free_form_selection.png
/usr/share/kolourpaint/icons/hicolor/32x32/actions/tool_line.png
/usr/share/kolourpaint/icons/hicolor/32x32/actions/tool_pen.png
/usr/share/kolourpaint/icons/hicolor/32x32/actions/tool_polygon.png
/usr/share/kolourpaint/icons/hicolor/32x32/actions/tool_polyline.png
/usr/share/kolourpaint/icons/hicolor/32x32/actions/tool_rect_selection.png
/usr/share/kolourpaint/icons/hicolor/32x32/actions/tool_rectangle.png
/usr/share/kolourpaint/icons/hicolor/32x32/actions/tool_rounded_rectangle.png
/usr/share/kolourpaint/icons/hicolor/32x32/actions/tool_spraycan.png
/usr/share/kolourpaint/icons/hicolor/32x32/actions/tool_text.png
/usr/share/kolourpaint/icons/hicolor/48x48/actions/tool_brush.png
/usr/share/kolourpaint/icons/hicolor/48x48/actions/tool_color_eraser.png
/usr/share/kolourpaint/icons/hicolor/48x48/actions/tool_color_picker.png
/usr/share/kolourpaint/icons/hicolor/48x48/actions/tool_curve.png
/usr/share/kolourpaint/icons/hicolor/48x48/actions/tool_ellipse.png
/usr/share/kolourpaint/icons/hicolor/48x48/actions/tool_elliptical_selection.png
/usr/share/kolourpaint/icons/hicolor/48x48/actions/tool_eraser.png
/usr/share/kolourpaint/icons/hicolor/48x48/actions/tool_flood_fill.png
/usr/share/kolourpaint/icons/hicolor/48x48/actions/tool_free_form_selection.png
/usr/share/kolourpaint/icons/hicolor/48x48/actions/tool_line.png
/usr/share/kolourpaint/icons/hicolor/48x48/actions/tool_pen.png
/usr/share/kolourpaint/icons/hicolor/48x48/actions/tool_polygon.png
/usr/share/kolourpaint/icons/hicolor/48x48/actions/tool_polyline.png
/usr/share/kolourpaint/icons/hicolor/48x48/actions/tool_rect_selection.png
/usr/share/kolourpaint/icons/hicolor/48x48/actions/tool_rectangle.png
/usr/share/kolourpaint/icons/hicolor/48x48/actions/tool_rounded_rectangle.png
/usr/share/kolourpaint/icons/hicolor/48x48/actions/tool_spraycan.png
/usr/share/kolourpaint/icons/hicolor/48x48/actions/tool_text.png
/usr/share/kolourpaint/icons/hicolor/scalable/actions/tool_brush.svgz
/usr/share/kolourpaint/icons/hicolor/scalable/actions/tool_color_eraser.svgz
/usr/share/kolourpaint/icons/hicolor/scalable/actions/tool_color_picker.svgz
/usr/share/kolourpaint/icons/hicolor/scalable/actions/tool_curve.svgz
/usr/share/kolourpaint/icons/hicolor/scalable/actions/tool_ellipse.svgz
/usr/share/kolourpaint/icons/hicolor/scalable/actions/tool_elliptical_selection.svgz
/usr/share/kolourpaint/icons/hicolor/scalable/actions/tool_eraser.svgz
/usr/share/kolourpaint/icons/hicolor/scalable/actions/tool_flood_fill.svgz
/usr/share/kolourpaint/icons/hicolor/scalable/actions/tool_free_form_selection.svgz
/usr/share/kolourpaint/icons/hicolor/scalable/actions/tool_line.svgz
/usr/share/kolourpaint/icons/hicolor/scalable/actions/tool_pen.svgz
/usr/share/kolourpaint/icons/hicolor/scalable/actions/tool_polygon.svgz
/usr/share/kolourpaint/icons/hicolor/scalable/actions/tool_polyline.svgz
/usr/share/kolourpaint/icons/hicolor/scalable/actions/tool_rect_selection.svgz
/usr/share/kolourpaint/icons/hicolor/scalable/actions/tool_rectangle.svgz
/usr/share/kolourpaint/icons/hicolor/scalable/actions/tool_rounded_rectangle.svgz
/usr/share/kolourpaint/icons/hicolor/scalable/actions/tool_spraycan.svgz
/usr/share/kolourpaint/icons/hicolor/scalable/actions/tool_text.svgz
/usr/share/kolourpaint/pics/color_transparent_26x26.png
/usr/share/kolourpaint/pics/colorbutton_swap_16x16.png
/usr/share/kolourpaint/pics/image_rotate_anticlockwise.png
/usr/share/kolourpaint/pics/image_rotate_clockwise.png
/usr/share/kolourpaint/pics/image_skew_horizontal.png
/usr/share/kolourpaint/pics/image_skew_vertical.png
/usr/share/kolourpaint/pics/option_opaque.png
/usr/share/kolourpaint/pics/option_transparent.png
/usr/share/kolourpaint/pics/resize.png
/usr/share/kolourpaint/pics/scale.png
/usr/share/kolourpaint/pics/smooth_scale.png
/usr/share/kolourpaint/pics/tool_spraycan_17x17.png
/usr/share/kolourpaint/pics/tool_spraycan_29x29.png
/usr/share/kolourpaint/pics/tool_spraycan_9x9.png
/usr/share/kxmlgui5/kolourpaint/kolourpaintui.rc
/usr/share/metainfo/org.kde.kolourpaint.appdata.xml

%files dev
%defattr(-,root,root,-)
/usr/lib64/libkolourpaint_lgpl.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kolourpaint/KolourPaint.png
/usr/share/doc/HTML/ca/kolourpaint/brush_shapes.png
/usr/share/doc/HTML/ca/kolourpaint/color_box.png
/usr/share/doc/HTML/ca/kolourpaint/eraser_shapes.png
/usr/share/doc/HTML/ca/kolourpaint/fcc_std_text.png
/usr/share/doc/HTML/ca/kolourpaint/fcc_trans_text.png
/usr/share/doc/HTML/ca/kolourpaint/fill_color_similarity.png
/usr/share/doc/HTML/ca/kolourpaint/fill_style.png
/usr/share/doc/HTML/ca/kolourpaint/image_balance.png
/usr/share/doc/HTML/ca/kolourpaint/image_emboss.png
/usr/share/doc/HTML/ca/kolourpaint/image_flatten.png
/usr/share/doc/HTML/ca/kolourpaint/image_invert.png
/usr/share/doc/HTML/ca/kolourpaint/image_reduce_colors.png
/usr/share/doc/HTML/ca/kolourpaint/image_resize_scale.png
/usr/share/doc/HTML/ca/kolourpaint/image_rotate.png
/usr/share/doc/HTML/ca/kolourpaint/image_skew.png
/usr/share/doc/HTML/ca/kolourpaint/image_soften_sharpen.png
/usr/share/doc/HTML/ca/kolourpaint/index.cache.bz2
/usr/share/doc/HTML/ca/kolourpaint/index.docbook
/usr/share/doc/HTML/ca/kolourpaint/line_width.png
/usr/share/doc/HTML/ca/kolourpaint/lines_30_45_deg.png
/usr/share/doc/HTML/ca/kolourpaint/lines_30_deg.png
/usr/share/doc/HTML/ca/kolourpaint/lines_45_deg.png
/usr/share/doc/HTML/ca/kolourpaint/rotate_image_30.png
/usr/share/doc/HTML/ca/kolourpaint/rotate_selection_30.png
/usr/share/doc/HTML/ca/kolourpaint/selections_opaque_transparent.png
/usr/share/doc/HTML/ca/kolourpaint/spraycan_patterns.png
/usr/share/doc/HTML/ca/kolourpaint/text_zoom_grid.png
/usr/share/doc/HTML/ca/kolourpaint/tool_brush.png
/usr/share/doc/HTML/ca/kolourpaint/tool_color_picker.png
/usr/share/doc/HTML/ca/kolourpaint/tool_color_washer.png
/usr/share/doc/HTML/ca/kolourpaint/tool_curve.png
/usr/share/doc/HTML/ca/kolourpaint/tool_ellipse.png
/usr/share/doc/HTML/ca/kolourpaint/tool_elliptical_selection.png
/usr/share/doc/HTML/ca/kolourpaint/tool_eraser.png
/usr/share/doc/HTML/ca/kolourpaint/tool_flood_fill.png
/usr/share/doc/HTML/ca/kolourpaint/tool_free_form_selection.png
/usr/share/doc/HTML/ca/kolourpaint/tool_line.png
/usr/share/doc/HTML/ca/kolourpaint/tool_pen.png
/usr/share/doc/HTML/ca/kolourpaint/tool_polygon.png
/usr/share/doc/HTML/ca/kolourpaint/tool_polyline.png
/usr/share/doc/HTML/ca/kolourpaint/tool_polystar.png
/usr/share/doc/HTML/ca/kolourpaint/tool_rect_selection.png
/usr/share/doc/HTML/ca/kolourpaint/tool_rectangle.png
/usr/share/doc/HTML/ca/kolourpaint/tool_rectangles.png
/usr/share/doc/HTML/ca/kolourpaint/tool_rounded_rectangle.png
/usr/share/doc/HTML/ca/kolourpaint/tool_selections.png
/usr/share/doc/HTML/ca/kolourpaint/tool_spraycan.png
/usr/share/doc/HTML/ca/kolourpaint/tool_text.png
/usr/share/doc/HTML/de/kolourpaint/KolourPaint.png
/usr/share/doc/HTML/de/kolourpaint/image_balance.png
/usr/share/doc/HTML/de/kolourpaint/image_emboss.png
/usr/share/doc/HTML/de/kolourpaint/image_flatten.png
/usr/share/doc/HTML/de/kolourpaint/image_flip.png
/usr/share/doc/HTML/de/kolourpaint/image_invert.png
/usr/share/doc/HTML/de/kolourpaint/image_reduce_colors.png
/usr/share/doc/HTML/de/kolourpaint/image_resize_scale.png
/usr/share/doc/HTML/de/kolourpaint/image_rotate.png
/usr/share/doc/HTML/de/kolourpaint/image_skew.png
/usr/share/doc/HTML/de/kolourpaint/image_soften_sharpen.png
/usr/share/doc/HTML/de/kolourpaint/index.cache.bz2
/usr/share/doc/HTML/de/kolourpaint/index.docbook
/usr/share/doc/HTML/en/kolourpaint/KolourPaint.png
/usr/share/doc/HTML/en/kolourpaint/brush_shapes.png
/usr/share/doc/HTML/en/kolourpaint/color_box.png
/usr/share/doc/HTML/en/kolourpaint/eraser_shapes.png
/usr/share/doc/HTML/en/kolourpaint/fcc_std_text.png
/usr/share/doc/HTML/en/kolourpaint/fcc_trans_text.png
/usr/share/doc/HTML/en/kolourpaint/fill_color_similarity.png
/usr/share/doc/HTML/en/kolourpaint/fill_style.png
/usr/share/doc/HTML/en/kolourpaint/image_balance.png
/usr/share/doc/HTML/en/kolourpaint/image_emboss.png
/usr/share/doc/HTML/en/kolourpaint/image_flatten.png
/usr/share/doc/HTML/en/kolourpaint/image_invert.png
/usr/share/doc/HTML/en/kolourpaint/image_reduce_colors.png
/usr/share/doc/HTML/en/kolourpaint/image_resize_scale.png
/usr/share/doc/HTML/en/kolourpaint/image_rotate.png
/usr/share/doc/HTML/en/kolourpaint/image_skew.png
/usr/share/doc/HTML/en/kolourpaint/image_soften_sharpen.png
/usr/share/doc/HTML/en/kolourpaint/index.cache.bz2
/usr/share/doc/HTML/en/kolourpaint/index.docbook
/usr/share/doc/HTML/en/kolourpaint/line_width.png
/usr/share/doc/HTML/en/kolourpaint/lines_30_45_deg.png
/usr/share/doc/HTML/en/kolourpaint/lines_30_deg.png
/usr/share/doc/HTML/en/kolourpaint/lines_45_deg.png
/usr/share/doc/HTML/en/kolourpaint/rotate_image_30.png
/usr/share/doc/HTML/en/kolourpaint/rotate_selection_30.png
/usr/share/doc/HTML/en/kolourpaint/screenshot_acquiring.png
/usr/share/doc/HTML/en/kolourpaint/selections_opaque_transparent.png
/usr/share/doc/HTML/en/kolourpaint/spraycan_patterns.png
/usr/share/doc/HTML/en/kolourpaint/text_zoom_grid.png
/usr/share/doc/HTML/en/kolourpaint/tool_brush.png
/usr/share/doc/HTML/en/kolourpaint/tool_color_picker.png
/usr/share/doc/HTML/en/kolourpaint/tool_color_washer.png
/usr/share/doc/HTML/en/kolourpaint/tool_curve.png
/usr/share/doc/HTML/en/kolourpaint/tool_ellipse.png
/usr/share/doc/HTML/en/kolourpaint/tool_elliptical_selection.png
/usr/share/doc/HTML/en/kolourpaint/tool_eraser.png
/usr/share/doc/HTML/en/kolourpaint/tool_flood_fill.png
/usr/share/doc/HTML/en/kolourpaint/tool_free_form_selection.png
/usr/share/doc/HTML/en/kolourpaint/tool_line.png
/usr/share/doc/HTML/en/kolourpaint/tool_pen.png
/usr/share/doc/HTML/en/kolourpaint/tool_polygon.png
/usr/share/doc/HTML/en/kolourpaint/tool_polyline.png
/usr/share/doc/HTML/en/kolourpaint/tool_polystar.png
/usr/share/doc/HTML/en/kolourpaint/tool_rect_selection.png
/usr/share/doc/HTML/en/kolourpaint/tool_rectangle.png
/usr/share/doc/HTML/en/kolourpaint/tool_rectangles.png
/usr/share/doc/HTML/en/kolourpaint/tool_rounded_rectangle.png
/usr/share/doc/HTML/en/kolourpaint/tool_selections.png
/usr/share/doc/HTML/en/kolourpaint/tool_spraycan.png
/usr/share/doc/HTML/en/kolourpaint/tool_text.png
/usr/share/doc/HTML/en/kolourpaint/view_thumbnails.png
/usr/share/doc/HTML/es/kolourpaint/brush_shapes.png
/usr/share/doc/HTML/es/kolourpaint/color_box.png
/usr/share/doc/HTML/es/kolourpaint/eraser_shapes.png
/usr/share/doc/HTML/es/kolourpaint/fcc_std_text.png
/usr/share/doc/HTML/es/kolourpaint/fcc_trans_text.png
/usr/share/doc/HTML/es/kolourpaint/fill_color_similarity.png
/usr/share/doc/HTML/es/kolourpaint/fill_style.png
/usr/share/doc/HTML/es/kolourpaint/image_balance.png
/usr/share/doc/HTML/es/kolourpaint/image_emboss.png
/usr/share/doc/HTML/es/kolourpaint/image_flatten.png
/usr/share/doc/HTML/es/kolourpaint/image_invert.png
/usr/share/doc/HTML/es/kolourpaint/image_reduce_colors.png
/usr/share/doc/HTML/es/kolourpaint/image_resize_scale.png
/usr/share/doc/HTML/es/kolourpaint/image_rotate.png
/usr/share/doc/HTML/es/kolourpaint/image_skew.png
/usr/share/doc/HTML/es/kolourpaint/image_soften_sharpen.png
/usr/share/doc/HTML/es/kolourpaint/index.cache.bz2
/usr/share/doc/HTML/es/kolourpaint/index.docbook
/usr/share/doc/HTML/es/kolourpaint/line_width.png
/usr/share/doc/HTML/es/kolourpaint/lines_30_45_deg.png
/usr/share/doc/HTML/es/kolourpaint/lines_30_deg.png
/usr/share/doc/HTML/es/kolourpaint/lines_45_deg.png
/usr/share/doc/HTML/es/kolourpaint/rotate_image_30.png
/usr/share/doc/HTML/es/kolourpaint/rotate_selection_30.png
/usr/share/doc/HTML/es/kolourpaint/selections_opaque_transparent.png
/usr/share/doc/HTML/es/kolourpaint/spraycan_patterns.png
/usr/share/doc/HTML/es/kolourpaint/text_zoom_grid.png
/usr/share/doc/HTML/es/kolourpaint/tool_brush.png
/usr/share/doc/HTML/es/kolourpaint/tool_color_picker.png
/usr/share/doc/HTML/es/kolourpaint/tool_color_washer.png
/usr/share/doc/HTML/es/kolourpaint/tool_curve.png
/usr/share/doc/HTML/es/kolourpaint/tool_ellipse.png
/usr/share/doc/HTML/es/kolourpaint/tool_elliptical_selection.png
/usr/share/doc/HTML/es/kolourpaint/tool_eraser.png
/usr/share/doc/HTML/es/kolourpaint/tool_flood_fill.png
/usr/share/doc/HTML/es/kolourpaint/tool_free_form_selection.png
/usr/share/doc/HTML/es/kolourpaint/tool_line.png
/usr/share/doc/HTML/es/kolourpaint/tool_pen.png
/usr/share/doc/HTML/es/kolourpaint/tool_polygon.png
/usr/share/doc/HTML/es/kolourpaint/tool_polyline.png
/usr/share/doc/HTML/es/kolourpaint/tool_polystar.png
/usr/share/doc/HTML/es/kolourpaint/tool_rect_selection.png
/usr/share/doc/HTML/es/kolourpaint/tool_rectangle.png
/usr/share/doc/HTML/es/kolourpaint/tool_rectangles.png
/usr/share/doc/HTML/es/kolourpaint/tool_rounded_rectangle.png
/usr/share/doc/HTML/es/kolourpaint/tool_selections.png
/usr/share/doc/HTML/es/kolourpaint/tool_spraycan.png
/usr/share/doc/HTML/es/kolourpaint/tool_text.png
/usr/share/doc/HTML/es/kolourpaint/view_thumbnails.png
/usr/share/doc/HTML/et/kolourpaint/index.cache.bz2
/usr/share/doc/HTML/et/kolourpaint/index.docbook
/usr/share/doc/HTML/fr/kolourpaint/index.cache.bz2
/usr/share/doc/HTML/fr/kolourpaint/index.docbook
/usr/share/doc/HTML/gl/kolourpaint/index.cache.bz2
/usr/share/doc/HTML/gl/kolourpaint/index.docbook
/usr/share/doc/HTML/it/kolourpaint/index.cache.bz2
/usr/share/doc/HTML/it/kolourpaint/index.docbook
/usr/share/doc/HTML/nl/kolourpaint/KolourPaint.png
/usr/share/doc/HTML/nl/kolourpaint/index.cache.bz2
/usr/share/doc/HTML/nl/kolourpaint/index.docbook
/usr/share/doc/HTML/pl/kolourpaint/fullscreen_mode.png
/usr/share/doc/HTML/pl/kolourpaint/image_balance.png
/usr/share/doc/HTML/pl/kolourpaint/image_emboss.png
/usr/share/doc/HTML/pl/kolourpaint/image_flatten.png
/usr/share/doc/HTML/pl/kolourpaint/image_flip.png
/usr/share/doc/HTML/pl/kolourpaint/image_invert.png
/usr/share/doc/HTML/pl/kolourpaint/image_reduce_colors.png
/usr/share/doc/HTML/pl/kolourpaint/image_resize_scale.png
/usr/share/doc/HTML/pl/kolourpaint/image_rotate.png
/usr/share/doc/HTML/pl/kolourpaint/image_skew.png
/usr/share/doc/HTML/pl/kolourpaint/image_soften_sharpen.png
/usr/share/doc/HTML/pl/kolourpaint/index.cache.bz2
/usr/share/doc/HTML/pl/kolourpaint/index.docbook
/usr/share/doc/HTML/pt/kolourpaint/index.cache.bz2
/usr/share/doc/HTML/pt/kolourpaint/index.docbook
/usr/share/doc/HTML/pt_BR/kolourpaint/KolourPaint.png
/usr/share/doc/HTML/pt_BR/kolourpaint/brush_shapes.png
/usr/share/doc/HTML/pt_BR/kolourpaint/color_box.png
/usr/share/doc/HTML/pt_BR/kolourpaint/eraser_shapes.png
/usr/share/doc/HTML/pt_BR/kolourpaint/fcc_std_text.png
/usr/share/doc/HTML/pt_BR/kolourpaint/fcc_trans_text.png
/usr/share/doc/HTML/pt_BR/kolourpaint/fill_color_similarity.png
/usr/share/doc/HTML/pt_BR/kolourpaint/fill_style.png
/usr/share/doc/HTML/pt_BR/kolourpaint/image_balance.png
/usr/share/doc/HTML/pt_BR/kolourpaint/image_emboss.png
/usr/share/doc/HTML/pt_BR/kolourpaint/image_flatten.png
/usr/share/doc/HTML/pt_BR/kolourpaint/image_invert.png
/usr/share/doc/HTML/pt_BR/kolourpaint/image_reduce_colors.png
/usr/share/doc/HTML/pt_BR/kolourpaint/image_resize_scale.png
/usr/share/doc/HTML/pt_BR/kolourpaint/image_rotate.png
/usr/share/doc/HTML/pt_BR/kolourpaint/image_skew.png
/usr/share/doc/HTML/pt_BR/kolourpaint/image_soften_sharpen.png
/usr/share/doc/HTML/pt_BR/kolourpaint/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kolourpaint/index.docbook
/usr/share/doc/HTML/pt_BR/kolourpaint/line_width.png
/usr/share/doc/HTML/pt_BR/kolourpaint/lines_30_45_deg.png
/usr/share/doc/HTML/pt_BR/kolourpaint/lines_30_deg.png
/usr/share/doc/HTML/pt_BR/kolourpaint/lines_45_deg.png
/usr/share/doc/HTML/pt_BR/kolourpaint/rotate_image_30.png
/usr/share/doc/HTML/pt_BR/kolourpaint/rotate_selection_30.png
/usr/share/doc/HTML/pt_BR/kolourpaint/screenshot_acquiring.png
/usr/share/doc/HTML/pt_BR/kolourpaint/selections_opaque_transparent.png
/usr/share/doc/HTML/pt_BR/kolourpaint/spraycan_patterns.png
/usr/share/doc/HTML/pt_BR/kolourpaint/text_zoom_grid.png
/usr/share/doc/HTML/pt_BR/kolourpaint/tool_brush.png
/usr/share/doc/HTML/pt_BR/kolourpaint/tool_color_picker.png
/usr/share/doc/HTML/pt_BR/kolourpaint/tool_color_washer.png
/usr/share/doc/HTML/pt_BR/kolourpaint/tool_curve.png
/usr/share/doc/HTML/pt_BR/kolourpaint/tool_ellipse.png
/usr/share/doc/HTML/pt_BR/kolourpaint/tool_elliptical_selection.png
/usr/share/doc/HTML/pt_BR/kolourpaint/tool_eraser.png
/usr/share/doc/HTML/pt_BR/kolourpaint/tool_flood_fill.png
/usr/share/doc/HTML/pt_BR/kolourpaint/tool_free_form_selection.png
/usr/share/doc/HTML/pt_BR/kolourpaint/tool_line.png
/usr/share/doc/HTML/pt_BR/kolourpaint/tool_pen.png
/usr/share/doc/HTML/pt_BR/kolourpaint/tool_polygon.png
/usr/share/doc/HTML/pt_BR/kolourpaint/tool_polyline.png
/usr/share/doc/HTML/pt_BR/kolourpaint/tool_polystar.png
/usr/share/doc/HTML/pt_BR/kolourpaint/tool_rect_selection.png
/usr/share/doc/HTML/pt_BR/kolourpaint/tool_rectangle.png
/usr/share/doc/HTML/pt_BR/kolourpaint/tool_rectangles.png
/usr/share/doc/HTML/pt_BR/kolourpaint/tool_rounded_rectangle.png
/usr/share/doc/HTML/pt_BR/kolourpaint/tool_selections.png
/usr/share/doc/HTML/pt_BR/kolourpaint/tool_spraycan.png
/usr/share/doc/HTML/pt_BR/kolourpaint/tool_text.png
/usr/share/doc/HTML/pt_BR/kolourpaint/view_thumbnails.png
/usr/share/doc/HTML/ru/kolourpaint/KolourPaint.png
/usr/share/doc/HTML/ru/kolourpaint/image_balance.png
/usr/share/doc/HTML/ru/kolourpaint/image_emboss.png
/usr/share/doc/HTML/ru/kolourpaint/image_flatten.png
/usr/share/doc/HTML/ru/kolourpaint/image_invert.png
/usr/share/doc/HTML/ru/kolourpaint/image_reduce_colors.png
/usr/share/doc/HTML/ru/kolourpaint/image_resize_scale.png
/usr/share/doc/HTML/ru/kolourpaint/image_rotate.png
/usr/share/doc/HTML/ru/kolourpaint/image_skew.png
/usr/share/doc/HTML/ru/kolourpaint/image_soften_sharpen.png
/usr/share/doc/HTML/ru/kolourpaint/index.cache.bz2
/usr/share/doc/HTML/ru/kolourpaint/index.docbook
/usr/share/doc/HTML/ru/kolourpaint/screenshot_acquiring.png
/usr/share/doc/HTML/ru/kolourpaint/view_thumbnails.png
/usr/share/doc/HTML/sv/kolourpaint/image_balance.png
/usr/share/doc/HTML/sv/kolourpaint/image_emboss.png
/usr/share/doc/HTML/sv/kolourpaint/image_flatten.png
/usr/share/doc/HTML/sv/kolourpaint/image_flip.png
/usr/share/doc/HTML/sv/kolourpaint/image_invert.png
/usr/share/doc/HTML/sv/kolourpaint/image_reduce_colors.png
/usr/share/doc/HTML/sv/kolourpaint/image_resize_scale.png
/usr/share/doc/HTML/sv/kolourpaint/image_rotate.png
/usr/share/doc/HTML/sv/kolourpaint/image_skew.png
/usr/share/doc/HTML/sv/kolourpaint/image_soften_sharpen.png
/usr/share/doc/HTML/sv/kolourpaint/index.cache.bz2
/usr/share/doc/HTML/sv/kolourpaint/index.docbook
/usr/share/doc/HTML/sv/kolourpaint/view_thumbnails.png
/usr/share/doc/HTML/uk/kolourpaint/KolourPaint.png
/usr/share/doc/HTML/uk/kolourpaint/image_balance.png
/usr/share/doc/HTML/uk/kolourpaint/image_emboss.png
/usr/share/doc/HTML/uk/kolourpaint/image_flatten.png
/usr/share/doc/HTML/uk/kolourpaint/image_invert.png
/usr/share/doc/HTML/uk/kolourpaint/image_reduce_colors.png
/usr/share/doc/HTML/uk/kolourpaint/image_resize_scale.png
/usr/share/doc/HTML/uk/kolourpaint/image_rotate.png
/usr/share/doc/HTML/uk/kolourpaint/image_skew.png
/usr/share/doc/HTML/uk/kolourpaint/image_soften_sharpen.png
/usr/share/doc/HTML/uk/kolourpaint/index.cache.bz2
/usr/share/doc/HTML/uk/kolourpaint/index.docbook
/usr/share/doc/HTML/uk/kolourpaint/screenshot_acquiring.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkolourpaint_lgpl.so.5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kolourpaint/COPYING.DOC
/usr/share/package-licenses/kolourpaint/COPYING.LIB

%files locales -f kolourpaint.lang
%defattr(-,root,root,-)

